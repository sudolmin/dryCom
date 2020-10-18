// alert('Working...')
function openNav() {
  document.getElementById("storeSidenav").style.width = "250px";
  document.body.style.backgroundColor = "rgba(0,0,0,0.4)";
}
if (document.getElementById("main")!==null){
	document.getElementById("main").addEventListener("click", closeNav);
}


function closeNav() {
  document.getElementById("storeSidenav").style.width = "0";
  document.body.style.backgroundColor = "#fcf7e9";
}

var updateBtns = document.getElementsByClassName('update-cart')
for(var i = 0; i < updateBtns.length; i++){
	updateBtns[i].addEventListener('click', function(){
		var productId = this.dataset.product
		var action = this.dataset.action

		if(user == 'AnonymousUser'){
			console.log('Not Logged In')
		}else{
			updateUserOrder(productId, action)
		}
	})
}

function updateUserOrder(productId, action){

	var url = '/updateItem/'

	fetch(url,{
		method:'POST', 
		headers:{
			'Content-Type':'application/json',
			'X-CSRFToken':csrftoken
		},
		body:JSON.stringify({'productId': productId, 'action':action})
	})
	.then((response) =>{
		return response.json()
	})
	.then((data) => {
		location.reload()
	})
}

cartItems()

function cartItems(){
	var itemId = document.getElementById('cart-total')
	var url = '/cart-api/'

	fetch(url)
	.then((resp) => resp.json())
	.then(function(data){
		
		for (var i = 0; i < data.length; i++) {
			if (data[i].complete==false) {
				itemId.innerHTML += String(data[i].get_cart_items)
			}
			
		}
	})
} 
