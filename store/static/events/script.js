// alert('Working...')
function openNav() {
  document.getElementById("storeSidenav").style.width = "250px";
  document.body.style.backgroundColor = "rgba(0,0,0,0.4)";
}

document.getElementById("main").addEventListener("click", closeNav);

function closeNav() {
  document.getElementById("storeSidenav").style.width = "0";
  document.body.style.backgroundColor = "#fcf7e9";
}

var updateBtns = document.getElementsByClassName('update-cart')
for(var i = 0; i < updateBtns.length; i++){
	updateBtns[i].addEventListener('click', function(){
		var productId = this.dataset.product
		var action = this.dataset.action
		console.log('productId:', productId, 'action:', action)

		console.log("USER:", user)
		if(user == 'AnonymousUser'){
			console.log('Not Logged In')
		}else{
			updateUserOrder(productId, action)
		}
	})
}

function updateUserOrder(productId, action){
	console.log('User is logged in, sending data...')

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
		console.log('data', data)
	})
}