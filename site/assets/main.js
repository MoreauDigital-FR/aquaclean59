/* Aqua Clean 59 — interactions */
(() => {
  const root = document.documentElement;
  root.classList.add("js");
  const reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* menu mobile */
  const toggle = document.querySelector(".nav-toggle");
  if (toggle) {
    toggle.addEventListener("click", () => {
      const open = root.classList.toggle("nav-open");
      toggle.setAttribute("aria-expanded", String(open));
    });
    document.querySelectorAll(".nav-links a").forEach((a) =>
      a.addEventListener("click", () => {
        root.classList.remove("nav-open");
        toggle.setAttribute("aria-expanded", "false");
      })
    );
  }

  /* apparitions au scroll */
  const pending = new Set(document.querySelectorAll(".reveal"));
  const reveal = () => {
    const limit = window.innerHeight * 0.92;
    pending.forEach((el) => {
      if (reduce || el.getBoundingClientRect().top < limit) {
        el.classList.add("in");
        pending.delete(el);
      }
    });
  };
  let ticking = false;
  const onReveal = () => {
    if (ticking) return;
    ticking = true;
    requestAnimationFrame(() => { reveal(); ticking = false; });
  };
  window.addEventListener("scroll", onReveal, { passive: true });
  window.addEventListener("resize", onReveal);
  reveal();

  /* vidéo hero : pas d'autoplay si mouvement réduit ou économie de données */
  const heroVideo = document.querySelector("[data-hero-video]");
  if (heroVideo) {
    const saveData = navigator.connection && navigator.connection.saveData;
    if (reduce || saveData) {
      heroVideo.removeAttribute("autoplay");
      heroVideo.pause();
    } else {
      heroVideo.play().catch(() => {});
    }
  }

  /* avant / après */
  document.querySelectorAll(".ba").forEach((ba) => {
    const range = ba.querySelector("input[type=range]");
    const set = (v) => ba.style.setProperty("--pos", v + "%");
    range.addEventListener("input", () => set(range.value));
    set(range.value);
  });

  /* barre d'appel mobile */
  const callbar = document.querySelector(".callbar");
  if (callbar) {
    const onScroll = () => callbar.classList.toggle("show", window.scrollY > 420);
    window.addEventListener("scroll", onScroll, { passive: true });
    onScroll();
  }

  /* onglets de tarifs */
  document.querySelectorAll("[data-tabs]").forEach((group) => {
    const buttons = group.querySelectorAll("[role=tab]");
    buttons.forEach((btn) => {
      btn.addEventListener("click", () => {
        buttons.forEach((b) => b.setAttribute("aria-selected", String(b === btn)));
        const target = btn.getAttribute("aria-controls");
        document.querySelectorAll(`[data-panel-group="${group.dataset.tabs}"]`).forEach((p) => {
          p.hidden = p.id !== target;
        });
      });
    });
  });

  /* demande de devis → SMS pré-rempli */
  const form = document.querySelector("[data-quote]");
  if (form) {
    const PHONE = "+33757468512";
    const PRICES = {
      "Voiture — petite": { "Intérieur": 80, "Intérieur + extérieur": 105 },
      "Voiture — moyenne": { "Intérieur": 90, "Intérieur + extérieur": 115 },
      "Voiture — grande": { "Intérieur": 100, "Intérieur + extérieur": 125 },
      "Utilitaire": { "Intérieur": 80, "Intérieur + extérieur": 120 },
      "Canapé 2/3 places": { "-": 70 },
      "Canapé 4/5 places": { "-": 85 },
      "Matelas 2 places": { "-": 75 },
      "Rénovation des phares": { "-": 70 },
    };
    const out = form.querySelector("[data-estimate]");
    const formulaField = form.querySelector("[data-formula]");

    const read = () => {
      const fd = new FormData(form);
      return {
        service: fd.get("service") || "",
        formula: fd.get("formula") || "",
        city: (fd.get("city") || "").trim(),
        name: (fd.get("name") || "").trim(),
        when: fd.get("when") || "",
        details: (fd.get("details") || "").trim(),
      };
    };

    const update = () => {
      const d = read();
      const table = PRICES[d.service];
      const needsFormula = table && !table["-"];
      formulaField.hidden = !needsFormula;
      let price = null;
      if (table) price = needsFormula ? table[d.formula] : table["-"];
      out.textContent = price ? (d.service === "Utilitaire" ? "dès " : "") + price + " €" : "—";
    };

    const message = () => {
      const d = read();
      const lines = [
        "Bonjour Aqua Clean, je souhaite un devis.",
        d.service && "Prestation : " + d.service + (d.formula && !formulaField.hidden ? " (" + d.formula + ")" : ""),
        d.city && "Commune : " + d.city,
        d.when && "Disponibilité : " + d.when,
        d.details && "Précisions : " + d.details,
        d.name && "— " + d.name,
      ];
      return lines.filter(Boolean).join("\n");
    };

    form.addEventListener("change", update);
    form.addEventListener("input", update);
    update();

    form.addEventListener("submit", (e) => {
      e.preventDefault();
      if (!form.reportValidity()) return;
      window.location.href = "sms:" + PHONE + "?&body=" + encodeURIComponent(message());
    });

    const copyBtn = form.querySelector("[data-copy]");
    if (copyBtn) {
      copyBtn.addEventListener("click", async () => {
        try {
          await navigator.clipboard.writeText(message());
          const label = copyBtn.textContent;
          copyBtn.textContent = "Message copié";
          setTimeout(() => (copyBtn.textContent = label), 2000);
        } catch (_) {}
      });
    }
  }

  /* année du footer */
  const y = document.querySelector("[data-year]");
  if (y) y.textContent = new Date().getFullYear();
})();
