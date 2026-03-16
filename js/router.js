async function loadPage(page) {
    const content = document.getElementById("content");

    try {
        const response = await fetch(`content/${page}.html`);
        let html = await response.text();

        // oprava ciest k obrázkom
        html = html.replace(/src="obrazky\//g, 'src="content/obrazky/');

        content.innerHTML = html;
    } catch {
        content.innerHTML = "<h2>Stránka neexistuje</h2>";
    } finally {
        // Na malých obrazovkách po kliknutí v menu presuň viewport na obsah.
        requestAnimationFrame(() => {
            content.scrollIntoView({ behavior: "smooth", block: "start" });
        });
    }
}

// pri načítaní stránky
function router() {
    const hash = window.location.hash.substring(1);
    if (hash) loadPage(hash);
    else loadPage("onas"); // predvolená stránka
}

window.addEventListener("hashchange", router);
window.addEventListener("load", router);

