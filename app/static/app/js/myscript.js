$('#slider1, #slider2, #slider3').owlCarousel({
    loop: true,
    margin: 20,
    responsiveClass: true,
    responsive: {
        0: {
            items: 1,
            nav: false,
            autoplay: true,
        },
        600: {
            items: 3,
            nav: true,
            autoplay: true,
        },
        1000: {
            items: 5,
            nav: true,
            loop: true,
            autoplay: true,
        }
    }
})

// ṇum of cart item 
function CartItem() {
    $.ajax({
        type: "GET",
        url: "/cart-item",
        dataType: "json",
        success: function (data) {
            console.log(data.data);
            $('.numCart').text(data.data);

            
        }
    });
  }
  CartItem();

// product qty plus
$('.plus-cart').click(function() {
    var id = $(this).attr("pid").toString()
    var eml = this.parentNode.children[2]
    $.ajax({
        type: "GET",
        url: "/plus-cart",
        dataType: "json",
        data: {
            prod_id:id
        },
        success: function (response) {
            eml.innerText = response.quantuty
            $("#amount").text(response.amount);
            $("#totalamount").text(response.totalamount);
            console.log(response);
        }
    });
})
// product qty plus end
// product qty minus
$('.minus-cart').click(function() {
    var id = $(this).attr("pid").toString()
    var eml = this.parentNode.children[2]
    $.ajax({
        type: "GET",
        url: "/minus-cart",
        dataType: "json",
        data: {
            prod_id:id
        },
        success: function (response) {
            
            eml.innerText = response.quantuty
            $("#amount").text(response.amount);
            $("#totalamount").text(response.totalamount);
            console.log(response);
        }
    });
})
// product qty minus end
// product remove
$('.remove-cart').click(function() {
    var id = $(this).attr("pid").toString()
    var eml = this
    $.ajax({
        type: "GET",
        url: "/remove-cart",
        dataType: "json",
        data: {
            prod_id:id
        },
        success: function (response) {
            CartItem();
            console.log(response);
            $("#amount").text(response.amount);
            $("#totalamount").text(response.totalamount);
           eml.parentNode.parentNode.parentNode.parentNode.remove();
        }
    });
})
// product remove end

