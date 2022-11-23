const height = document.querySelector("#height");
const weight = document.querySelector("#weight");
const calculate = document.querySelector("#calculate");
const yourBMI = document.querySelector("#yourBMI");
const bmiresult = document.querySelector("#bmiinfo");
const minHt = 40;
const minWt = 4;
var msg = ``;
calculate.addEventListener("click", () => {
    //BMI = Body Mass Index
    //m = Mass Means Weight (KG)
    //h = Height (CM)
    //Formula = B = m/h²
    EnteredHeight = parseInt(height.value);
    EnteredWeight = parseInt(weight.value);
    console.log(EnteredHeight);

    if (height.value == "" && weight.value == "")
        yourBMI.innerHTML = `No value entered`;
    else if (!(Number.isInteger(EnteredHeight) && Number.isInteger(EnteredWeight)))
        yourBMI.innerHTML = `Please enter integer value`;
    else if ((height.value > minHt && weight.value > minWt)) {
        let bmiValue = weight.value / (height.value * height.value) * 10000;
        bmiValue = bmiValue.toFixed(2);
        yourBMI.innerHTML = `Your BMI Is : <span> ${bmiValue} </span>`
        let res = "";
        if (bmiValue < 18.5)
            res = "Under Weight";
        else if (bmiValue >= 18.5 && bmiValue < 25)
            res = "Normal Weight";
        else if (bmiValue >= 25 && bmiValue < 30)
            res = "Over Weight";
        else if (bmiValue >= 30)
            res = "Obese";
        bmiresult.innerHTML = `You are <span> ${res} </span>`


    } else {
        yourBMI.innerHTML = `Please Enter Correct Value`;
    }
});