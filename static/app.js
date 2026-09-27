// Client-side search over assessed entries and the separate unassessed idea pool.
(function () {
  var input = document.getElementById('search');
  var box = document.getElementById('search-results');
  var root = input ? input.dataset.root || '' : '';
  var data = null;

  function load(cb) {
    if (data) return cb(data);
    Promise.all([
      fetch(root + 'index.json').then(function (r) { return r.json(); }).catch(function () { return []; }),
      fetch(root + 'ideas.json').then(function (r) { return r.json(); }).catch(function () { return []; })
    ]).then(function (parts) {
      data = parts[0].concat(parts[1].map(function (i) {
        return { title: i.title, title_zh: i.title_zh, summary: i.question,
          type: 'proposed ' + i.type, url: 'ideas.html#' + i.id, tags: [i.domain] };
      }));
      cb(data);
    });
  }
  function score(e, q) {
    var hay = (e.title + ' ' + (e.title_zh || '') + ' ' + e.summary + ' ' + (e.summary_zh || '') + ' ' + (e.tags || []).join(' ')).toLowerCase();
    var s = 0;
    q.split(/\s+/).forEach(function (w) { if (w && hay.indexOf(w) >= 0) s += (e.title.toLowerCase().indexOf(w) >= 0 ? 3 : 1); });
    return s;
  }
  if (input) {
    input.addEventListener('input', function () {
      var q = input.value.trim().toLowerCase();
      if (!q) { box.hidden = true; return; }
      load(function (d) {
        if (input.value.trim().toLowerCase() !== q) return;
        var hits = d.map(function (e) { return [score(e, q), e]; }).filter(function (x) { return x[0] > 0; })
          .sort(function (a, b) { return b[0] - a[0]; }).slice(0, 12);
        box.replaceChildren();
        hits.forEach(function (x) {
          var e = x[1];
          var link = document.createElement('a');
          link.href = root + e.url;
          link.textContent = e.title;
          if (e.verdict) {
            var badge = document.createElement('span');
            badge.className = 'badge v-' + e.verdict;
            badge.textContent = e.verdict;
            link.append(' ', badge);
          }
          var detail = document.createElement('small');
          detail.textContent = e.type + ' · ' + e.summary.slice(0, 120);
          link.append(detail);
          box.append(link);
        });
        if (!hits.length) {
          var empty = document.createElement('p');
          empty.textContent = 'No results';
          box.append(empty);
        }
        box.hidden = false;
      });
    });
    document.addEventListener('click', function (ev) { if (!box.contains(ev.target) && ev.target !== input) box.hidden = true; });
  }
  var filters = document.querySelector('.filters');
  if (filters) {
    filters.addEventListener('change', function () {
      var on = {};
      filters.querySelectorAll('input:checked').forEach(function (c) { on[c.value] = true; });
      document.querySelectorAll(filters.dataset.filterTarget).forEach(function (card) {
        var v = card.dataset.verdict;
        card.style.display = (!v || on[v]) ? '' : 'none';
      });
    });
  }
})();
