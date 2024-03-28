const inputArr = ['age', 'trestbps', 'chol', 'thalach', 'oldpeak'];
const selectArr = ['sex', 'cp', 'fbs', 'restecg', 'exang', 'slope', 'ca', 'thal'];

setInterval(() => {
    let flag = 1;

    for(let item of inputArr) { 
        document.getElementById(item).addEventListener('focus', (event) => {
            event.target.style.border = "1px solid #36454F";
        })  

        document.getElementById(item).addEventListener('focusout', (event) => {
            if(event.target.value === '') {
                event.target.style.border = "1px dotted #CD5C5C";
            }
            else {
                event.target.style.border = null;
            }
        })  

        if(document.getElementById(item).value === '') {
            flag = 0;
        }
    }

    // console.log(flag);

    for(let item of selectArr) {
        document.getElementById(item).addEventListener('focus', (event) => {
            event.target.style.border = "1px solid #36454F";
        }) 

        document.getElementById(item).addEventListener('focusout', (event) => {
            if(event.target.value === '-1') {
                event.target.style.border = "1px dotted #CD5C5C";
                // event.target.style.background = "red";
            }
            else {
                event.target.style.border = null;
            }
        })  

        if(document.getElementById(item).value === '-1') {
            flag = 0;
        }
    }

    if(flag === 1) {
        let temp = document.getElementById('submit')
        temp.disabled = false;
        temp.style.opacity = 1;
        // temp.style.outline = none;
        
        temp.addEventListener('mouseenter', (event) => {
            event.target.style.color = "hsl(9, 59%, 34%)";
        })

        temp.addEventListener('mousedown', (event) => {
            event.target.style.color = "hsl(9, 59%, 44%)";
        })

        temp.addEventListener('mouseleave', (event) => {
            event.target.style.color = "#36454F";
        })
    }
    else {
        let temp = document.getElementById('submit')
        temp.disabled = true;
        temp.style = null;
    }
})



