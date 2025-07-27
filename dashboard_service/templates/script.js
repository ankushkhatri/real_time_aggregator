// === Crypto Price Integration ===
const previousPrices = {
  BTCUSDT: null,
  ETHUSDT: null,
  BNBUSDT: null,
};

function updatePrice(id, symbol, newPrice) {
  const span = document.getElementById(id);
  const oldPrice = previousPrices[symbol];

  span.textContent = parseFloat(newPrice).toFixed(4);

  if (oldPrice !== null) {
    if (newPrice > oldPrice) {
      span.className = 'green';
    } else if (newPrice < oldPrice) {
      span.className = 'red';
    } else {
      span.className = '';
    }
  }

  previousPrices[symbol] = newPrice;
}

async function fetchPrices() {
  try {
    const symbols = ['BTCUSDT', 'ETHUSDT', 'BNBUSDT'];
    for (let symbol of symbols) {
      const response = await fetch(`http://localhost:5000/crypto/${symbol}`);
      const data = await response.json();
      if (!data.error) {
        let spanId =
          symbol === 'BTCUSDT'
            ? 'btc-price'
            : symbol === 'ETHUSDT'
            ? 'eth-price'
            : 'bnb-price';
        updatePrice(spanId, symbol, parseFloat(data.price));
      }
    }
  } catch (error) {
    console.error('Error fetching prices:', error);
  }
}

// === Navigation and Other Sections ===
function showSection(id) {
  document.querySelectorAll('main section').forEach(sec => {
    sec.classList.remove('active');
  });
  document.getElementById(id).classList.add('active');
  if (window.innerWidth < 700) toggleNav(true);
}
function toggleNav(forceHide) {
  const links = document.querySelector('.nav-links');
  if (forceHide || links.classList.contains('show')) {
    links.classList.remove('show');
  } else {
    links.classList.add('show');
  }
}
window.onclick = function (e) {
  if (!e.target.matches('.nav-toggle')) {
    document.querySelector('.nav-links').classList.remove('show');
  }
};

// === Sources Section (placeholder demo logic) ===
function fetchSources() {
  // Replace with your backend call
  return Promise.resolve([
    { name: 'News API', status: 'active' },
    { name: 'Twitter API', status: 'active' },
    { name: 'Weather API', status: 'active' },
  ]);
}
function loadSources() {
  const list = document.getElementById('sources-list');
  fetchSources().then(sources => {
    list.innerHTML = sources
      .map(s => `<li>${s.name} <span>[${s.status}]</span></li>`)
      .join('');
  });
}

// === Settings Section Demo ===
document.getElementById('settings-form').onsubmit = function (e) {
  e.preventDefault();
  const interval = document.getElementById('interval').value;
  alert('Settings saved. Update interval: ' + interval + ' seconds.');
  // Save to backend/localStorage as needed
};

// === Initial load ===
window.addEventListener('DOMContentLoaded', () => {
  fetchPrices();
  setInterval(fetchPrices, 1000); // Live price every second
  loadSources();
});
