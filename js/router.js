async function loadPage(page) {
    const content = document.getElementById("content");

    try {
        const response = await fetch(`content/${page}.html`);
        const html = await response.text();
        content.innerHTML = html;
    } catch {
        content.innerHTML = "<h2>Stránka neexistuje</h2>";
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
