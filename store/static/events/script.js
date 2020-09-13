// alert('Working...')
function openNav() {
  document.getElementById("storeSidenav").style.width = "250px";
  document.body.style.backgroundColor = "rgba(0,0,0,0.4)";
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
		console.log('productId:', productId, 'action:', action)

		console.log("USER:", user)
		if(user == 'AnonymousUser'){
			console.log('Not Logged In')
		}else{
			console.log('User is logged in, sending data.')
		}
	})
}