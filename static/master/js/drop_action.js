function toggleDropdown() {
            document.getElementById("options").classList.toggle("show");
        }

function toggleDropdown_aux() {
            document.getElementById("options-aux").classList.toggle("show");
}

 window.onclick = function(event) {
            if (!event.target.matches('.dropdown button')) {
                let dropdowns = document.getElementsByClassName("dropdown-content");
                for (let i = 0; i < dropdowns.length; i++) {
                    let openDropdown = dropdowns[i];
                    if (openDropdown.classList.contains('show')) {
                        openDropdown.classList.remove('show');
                    }
                }
            }
 }

 window.onclick = function(event) {
    if (!event.target.matches('.dropdown-aux button')) {
        let dropdowns = document.getElementsByClassName("dropdown-content-aux");
        for (let i = 0; i < dropdowns.length; i++) {
            let openDropdown = dropdowns[i];
            if (openDropdown.classList.contains('show')) {
                openDropdown.classList.remove('show');
            }
        }
    }
}

 document.querySelectorAll('.dropdown-content input[type="checkbox"]').forEach(checkbox => {
            checkbox.addEventListener('change', function() {
                const text = this.value;
                const selectedItems = document.querySelector('.selected-items');
                console.log(selectedItems)
                const existingItem = selectedItems.querySelector(`[data-value="${text}"]`);

                if (this.checked) {
                    if (!existingItem) {
                        const selectedItem = document.createElement('div');
                        selectedItem.setAttribute('data-value', text);
                        selectedItem.innerText = text;
                        selectedItems.appendChild(selectedItem);
                    }
                } else {
                    if (existingItem) {
                        existingItem.remove();
                    }
                }
            });
        });

 document.querySelectorAll('.dropdown-content-aux input[type="checkbox"]').forEach(checkbox => {
            checkbox.addEventListener('change', function() {
                const text = this.value;
                

                const selectedItems = document.querySelector('.selected-items-aux');
                const existingItem = selectedItems.querySelector(`[data-value="${text}"]`);
         
                console.log("Ali "+existingItem)

                if (this.checked) {
                    if (!existingItem) {
                        const selectedItem = document.createElement('div');
                        selectedItem.setAttribute('data-value', text);
                        selectedItem.innerText = text;
                        selectedItems.appendChild(selectedItem);
                    }
                } else {
                    if (existingItem) {
                        existingItem.remove();
                    }
                }
            });
});