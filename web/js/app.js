const API_BASE = "http://localhost:8000";
const userId = 1;

// static product list (later fetch from backend)
const products = [
  { id: 1, name: "iPhone" },
  { id: 2, name: "MacBook" },
  { id: 3, name: "AirPods" },
  { id: 4, name: "Nike Shoes" }
];

// render products
function renderProducts() {
  const grid = document.getElementById("productGrid");

  grid.innerHTML = "";

  products.forEach(p => {
    const card = document.createElement("div");
    card.className = "card";

    card.innerHTML = `
      <h3>${p.name}</h3>
      <button class="btn" onclick="clickProduct(${p.id})">View</button>
    `;

    grid.appendChild(card);
  });
}

// simulate click
async function clickProduct(productId) {
  console.log("clicked:", productId);

  // later: send to backend
  // await fetch('/click', { method: 'POST' })

  loadRecommendations();
}

// fetch recommendations
async function loadRecommendations() {
  try {
    const res = await fetch(`${API_BASE}/recommend/${userId}`);
    const data = await res.json();

    const grid = document.getElementById("recommendGrid");
    grid.innerHTML = "";

    data.forEach(p => {
      const card = document.createElement("div");
      card.className = "card";

      card.innerHTML = `<h3>${p.name}</h3>`;

      grid.appendChild(card);
    });

  } catch (err) {
    console.error("API error:", err);
  }
}

// init
renderProducts();
loadRecommendations();