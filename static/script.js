/// ====================
// LOGIN
// ====================

const loginForm = document.getElementById("loginForm");

if(loginForm){

loginForm.addEventListener("submit", async (e) => {

    e.preventDefault();

    const username =
    document.getElementById("username").value;

    const password =
    document.getElementById("password").value;

    const response = await fetch("/login", {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({
            username,
            password
        })
    });

    const data = await response.json();

    document.getElementById("message")
    .innerText = data.message;

    if(response.ok){
        document.getElementById("message").style.color = "#22c55e";
    }else{
        document.getElementById("message").style.color = "#ef4444";
    }

});
}

// ====================
// PRODUCTS
// ====================

const productList =
document.getElementById("product-list");

if(productList){

fetch("/products")
.then(res => res.json())
.then(products => {

    products.forEach(product => {

        productList.innerHTML += `
            <div class="card">
                <h3>${product.name}</h3>
                <p>$${product.price}</p>
            </div>
        `;
    });

});
}

// ====================
// ORDERS
// ====================

const checkoutBtn =
document.getElementById("checkout-btn");

if(checkoutBtn){

checkoutBtn.addEventListener("click", async () => {

    const response = await fetch("/orders", {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({
            products: [1,2],
            total: 1250
        })
    });

    const data = await response.json();

    document.getElementById("order-msg")
    .innerText = data.message;

});
}