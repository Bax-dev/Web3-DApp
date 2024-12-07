 // Create 90 tiny circles and append to the body
 for (let i = 0; i < 100; i++) {
    const circle = document.createElement("div");
    circle.classList.add("circle");

    // Randomize position for each circle
    circle.style.top = `${Math.random() * 100}vh`;
    circle.style.left = `${Math.random() * 100}vw`;

    // Append the circle to the body
    document.body.appendChild(circle);
}

async function donate() {
    const address = document.getElementById("donorAddress").value;
    const amount = document.getElementById("donationAmount").value;
    await fetch("http://127.0.0.1:5000/donate", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ address, amount }),
    });
    alert("Donation Successful!");
}
async function distributeFunds() {
    await fetch("http://127.0.0.1:5000/distribute", { method: "POST" });
    alert("Funds Distributed!");
}
document.getElementById("donationForm").addEventListener("submit", function (e) {
    e.preventDefault();
    donate();
});