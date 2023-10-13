document.addEventListener("DOMContentLoaded", handleDOMContentLoaded);

function handleDOMContentLoaded(event) {
    // console.log(event.target)
    const form = document.querySelector("form")
    form.addEventListener("submit", (event) => {
        handleForm(event);
    })
}

function handleForm(event) {
    event.preventDefault()
    const locationInput = document.querySelector("#locationInput").value
    // console.log(event.target)
    fetchMechanics(locationInput)
}

function fetchMechanics(locationInput) {
    fetch("http://localhost:3000/Mechanics")
        .then(res => res.json())
        .then(data => {
            handleData(data, locationInput)

        })
}

function handleData(data, locationInput) {
    const filteredMech = data.filter((mech) => {
        return mech.location === locationInput;
    })
    // console.log(filteredMech)
    displayData(filteredMech)
}

function displayData(filteredMech) {
    const groupMechanics = document.querySelector(".group-mechanics")
    groupMechanics.innerHTML=''
    filteredMech.forEach((item) => {
        const {img, name, location} = item
        const mechanic = document.createElement("section")
        mechanic.innerHTML = `
    
    <div class="mechanic-card">
                <img src="${img}" alt="image alt" style="width: 300px; margin: auto;">
                <div>
                    <span><label for="name">Name </label>
                        <p>: ${name}</p>
                    </span>
                    <span><label for="location">Location </label>
                        <p>: ${location}</p>
                    </span>
                    <span><label for="contact">Contact </label>
                        <p>: martbwogo@gmail.com</p>
                    </span>
                    <span><label for="rate">Rate/Hr[Ksh] </label>
                        <p>: 500</p>
                    </span>
                </div>
                <button>Send Request</button>
            </div>
    `;
    groupMechanics.appendChild(mechanic)
    })


}