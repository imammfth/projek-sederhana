let angka1 = "";
let angka2 = "";
let operatorAktif = "";
const layar = document.getElementById("display");

function klikAngka(angka) {
    if (operatorAktif === "") {
        angka1 += angka;
        layar.value = angka1;
    } else {
        angka2 += angka;
        layar.value = angka1 + " " + operatorAktif + " " + angka2;
    }
}

function klikOperator(operator) {
    if (angka1 === "") return; 

    operatorAktif = operator;
    if (operator === "akar") {
        layar.value = "√" + angka1; 
    } else {
        layar.value = angka1 + " " + operatorAktif + " ";
    }
}

function hapusLayar() {
    angka1 = "";
    angka2 = "";
    operatorAktif = "";
    layar.value = "";
}

async function hitungHasil() {
    if (angka1 === "") return;

    let hasil = await eel.proses_hitung(angka1, angka2, operatorAktif)();

    layar.value = hasil;

    angka1 = hasil.toString();
    angka2 = "";
    operatorAktif = "";
}