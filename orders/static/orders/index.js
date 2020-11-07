document.addEventListener('DOMContentLoaded', ()=>{
	if (document.querySelector(".addtocart")) {
		document.querySelectorAll(".addtocart").forEach(cart =>{
			cart.onclick = function(){
				var item, username, item1, item2;
				var id = this.dataset.id;
				var input1 = document.querySelector(`#${id}input1`);
				var input2 = document.querySelector(`#${id}input2`);
				var success = document.querySelector('#alert-success');
				if(input1){
					if(input1.checked === true){
						item = document.querySelector(`#${id}name`).dataset.item;
						cat = document.querySelector(`#${id}name`).dataset.cat;
						username = document.querySelector(`#${id}name`).dataset.username;
						item1 = document.querySelector(`#${id}input1`).dataset.item1;
						quantity1 = document.querySelector(`#${id}quantity1`).value;
						console.log("checked");
					}
				}
				if(input2){
					if(input2.checked === true){
						item = document.querySelector(`#${id}name`).dataset.item;
						cat = document.querySelector(`#${id}name`).dataset.cat;
						username = document.querySelector(`#${id}name`).dataset.username;
						item2 = document.querySelector(`#${id}input2`).dataset.item2;
						quantity2 = document.querySelector(`#${id}quantity2`).value;
						console.log("checked2")
					}
				}
				if(document.querySelector(`#select${id}`)){
					username = document.querySelector(`#select${id}`).dataset.username;
					cat = document.querySelector(`#select${id}`).dataset.cat;
					item = document.querySelector(`#select${id}`).value;
				}
				const request = new XMLHttpRequest();
				if(!item1){
					item1="empty";
					quantity1=0;
				}

				if(!item2){
					item2 = "empty";
					quantity2=0;
				}

				username = username.toString();
				cat = cat.toString();
				item = item.toString();
				item1 = item1.toString();
				quantity1 = parseInt(quantity1);
				item2 = item2.toString();
				quantity2 = parseInt(quantity2);
				request.open('GET', `/addtocart/${username}/${cat}/${item}/${item1}/${quantity1}/${item2}/${quantity2}`);
				request.onload = () =>{
					var res = request.response;
					success.style.display = "block";
					success.innerHTML= res;
					
				};
				request.send();
				setTimeout(function(){ success.style.display="none"; }, 2000);
			}
		});
	}
	if(document.querySelector('.cancelorder')){
		document.querySelectorAll('.cancelorder').forEach(order=>{
			order.onclick = function(){
				const request = new XMLHttpRequest();
				var cancelorder = document.querySelector('#removed');
				var orderid = this.dataset.id;
				var cart = "no";
				request.open('GET', `/cancelorder/${orderid}/${cart}`);
				request.onload = ()=>{
					var res = request.response;
					cancelorder.style.display = "block";
					cancelorder.innerHTML = res;
				};
				request.send();
				document.querySelector(`#block${orderid}`).remove();
				setTimeout(function(){ cancelorder.style.display="none"; }, 2000);
			};
		});
	}

	if(document.querySelector('.removeorder')){
		document.querySelectorAll('.removeorder').forEach(order =>{
			order.onclick = function(){
				const request = new XMLHttpRequest();
				var orderid = this.dataset.id;
				var cart = "yes"
				request.open('GET', `/cancelorder/${orderid}/${cart}`);
				request.onload = ()=>{
					console.log(request.response);
				};
				request.send();
				document.querySelectorAll(`.row${orderid}`).forEach(ele =>{
					ele.remove();
				});
			};
		});
	}
});