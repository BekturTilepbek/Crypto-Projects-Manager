function onLoad() {
    let buttons = document.querySelectorAll('[data-js="delete_btn"]');
    for (let btn of buttons) {
        btn.addEventListener("click", function () {
            let deleteForm = document.getElementById('deleteForm');
            deleteForm.action = this.dataset.url;
            let deleteModal = document.getElementById('delete_modal');
            let modal = new bootstrap.Modal(deleteModal);
            modal.show();
        });
    }
}

window.addEventListener("load", onLoad);
