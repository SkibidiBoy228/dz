document.addEventListener("DOMContentLoaded", function () {

    const btn = document.getElementById("btn-seed");
    const result = document.getElementById("seed-result");

    btn.addEventListener("click", function () {
        result.innerHTML = `
            <div class="alert alert-warning alert-dismissible fade show" role="alert">
                <strong>Попередження!</strong> Ця дія небезпечна. Підтвердити?
                <button id="seed-confirm" class="btn btn-sm btn-danger ms-3">Так</button>
                <button id="seed-cancel" class="btn btn-sm btn-secondary ms-2">Ні</button>
            </div>
        `;
        document.getElementById("seed-confirm").onclick = function () {
            
            result.innerHTML = `
                <div class="alert alert-info">Виконується...</div>
            `;

            fetch("/seed/", { method: "PATCH" })
                .then(r => r.json())
                .then(j => {
                    result.innerHTML = `
                        <div class="alert alert-success alert-dismissible fade show">
                            <strong>Готово!</strong><br>
                            Status: <b>${j.status}</b><br>
                            User: <b>${j.user}</b>
                        </div>
                    `;
                })
                .catch(err => {
                    result.innerHTML = `
                        <div class="alert alert-danger">
                            <strong>Помилка:</strong> ${err}
                        </div>
                    `;
                });
        };

        document.getElementById("seed-cancel").onclick = function () {
            result.innerHTML = `
                <div class="alert alert-secondary">Скасовано.</div>
            `;
        };

    });

});
