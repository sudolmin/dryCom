

cate()

function cate(){
	// var itemId = document.getElementById('cart-total')
	var slider = document.getElementById("myRange");
	var output = document.getElementById("demo");
	output.innerHTML = slider.value;

	slider.oninput = function() {
	  output.innerHTML = this.value;
	}
	var url = '/category-api/'

	fetch(url)
	.then((resp) => resp.json())
	.then(function(data){
		max=min=Number(data[0]['Products'][0]['items'][0]['price'])
		for (var i = 0; i < data.length; i++) {
			for(var j = 0; j < data[i]['Products'].length; j++){
				for(var k = 0; k < data[i]['Products'][j]['items'].length; k++){
					itPrice=Number(data[i]['Products'][j]['items'][k]['price'])
					if(max<itPrice){max=itPrice}
					if(min>itPrice){min=itPrice}
					console.log(max, min)
				}
			}
		}
		slider.max=max;
		slider.min=min;
		// console.log(slider.max) 
	})
} 