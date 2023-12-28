document.addEventListener('DOMContentLoaded', function () {

    const edit_btn = document.getElementById("edit-btn");

    edit_btn.addEventListener('click', function (){
    const cells = document.querySelectorAll(".scores");
    cells.forEach(function(cell) {
        cell.contentEditable=true});
    this.style.display = 'none';
    });

    // The test cell colors bg if value is not right
    const testCells = document.getElementsByClassName('cell');
    for (let i = 0; i < testCells.length; i++) {
        testCells[i].addEventListener('blur', function () {
        // Handle the input event here
        console.log("Content changed:", this.innerText);

        value = +this.innerText;
        isValid = !isNaN(value);

        if (isValid) {
        
        if (value < 0 || value > 10) {
            this.style.backgroundColor = 'red';
            this.style.color = 'white';

        } else {
            this.style.backgroundColor = 'white';
            this.style.color = 'black';
        // will later refactor this to enable toggling of the bg.
        }
        } else {
            console.log(`Invalid value assigned to cell.innerText ${this.innerText}`);
            this.style.backgroundColor = 'red';
            this.style.color = 'white';
        }
        });
    }

    // The exam cell colors bg if value is not right
    const examCells = document.getElementsByClassName('exam-cell');
    for (let i = 0; i < examCells.length; i++) {
        examCells[i].addEventListener('blur', function () {
        // Handle the input event here
        console.log("Content changed:", this.innerText);

        value = +this.innerText;
        isValid = !isNaN(value);

        if (isValid) {
        
        if (value < 0 || value > 70) {
            this.style.backgroundColor = 'red';
            this.style.color = 'white';

        } else {
            this.style.backgroundColor = 'white';
            this.style.color = 'black';
        // will later refactor this to enable toggling of the bg.
        }
        } else {
            console.log(`Invalid value assigned to cell.innerText ${this.innerText}`);
            this.style.backgroundColor = 'red';
            this.style.color = 'white';
        }
        });
    }


    // Collects the data after all changes has been made
    const button = document.getElementById('button');
    button.addEventListener('click', function () {
        console.log('here for the btn');
        // function to collect all datas
        function saveData() {
            const data_arr = {};
            const tbody = table.getElementsByTagName('tbody')[0];
            const token = tbody.querySelector('input[type=hidden]').value;
            console.log(tbody);
            const rows = table.getElementsByTagName('tr');
            for (let i = 1; i < rows.length; i++) {
                const cells = rows[i].getElementsByTagName('td');
                const ca_id = rows[i].dataset.id;
                for (let i = 2; i < cells.length; i++) {
                    if (cells[i].style.backgroundColor == 'red') {
                        alert('The inputs are not correctly formatted');
                        // find a way to make this break the process of submitting the scores
                        break;
                    };
                };
                const rowData = {
                    first_ca: cells[1].innerText,
                    second_ca: cells[2].innerText,
                    third_ca: cells[3].innerText,
                    exams: cells[4].innerText
                };
                data_arr[ca_id] = rowData;
            };
        
            console.log('Data Arr: ', data_arr);

            // sendDataToBackend(data_arr);
            return data_arr;
        }
         data = saveData();

        sendDataToBackend(data);
        
        function sendDataToBackend(saveData) {
            console.log('sending data to backend: ', saveData);
            fetch('/record/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrfToken,
                },
                body: JSON.stringify(saveData,)
            }
            )
            .then(res => res.json())
            .then(data => {
                console.log('data:', data);
                setTimeout(function() {
                    location.reload();
                  }, 500);
            })
            .catch(err => {console.error(err);});
        
                }
    });
}

);