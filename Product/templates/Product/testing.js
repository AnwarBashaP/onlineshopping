

$.ajax({
            url: baseurl,
            type: 'POST',
            data: form_data,
            dataype: 'json',
            cache: false,
            contentType: false,
            processData: false,
            success: function (responsedata) {
            debugger
            console.log(responsedata.Alternativefilter)
                $('#list-view').html('');
                $('#inside-grid-view').html('');
                var count = responsedata.count
                var data = responsedata.products
                $('#alternativefilter').val(responsedata.Alternativefilter);
                console.log($('#alternativefilter').val(responsedata.Alternativefilter))
                $('#countdata').html('')
                $('#searchfilters').val('');
                console.log(count)
                $('#countdata').html("Showing all "+count+" results")
                $.each(data, function (key, value) {

                var html ="<div class='list-view-box'><div class='row'><div class='col-sm-6 col-md-6 col-lg-4 col-xl-4'><div class='products-single fix'><div class='box-img-hover'><div class='type-lb'><p class="+ value['Offer'] +">"+value['Offer']+"</p></div><img src="+value['ProductImage']+" class='img-fluid' alt='Image'><div class='mask-icon'><ul><li><a href='induvialProduct/'"+value['slug']+" data-toggle='tooltip' data-placement='right' title='View'><i class='fas fa-eye'></i></a></li><li><a href='#' data-toggle='tooltip' data-placement='right' title='Compare'><i class='fas fa-sync-alt'></i></a></li><li><a href='#' data-toggle='tooltip' data-placement='right' title='Add to Wishlist'><i class='far fa-heart'></i></a></li></ul></div></div></div></div><div class='col-sm-6 col-md-6 col-lg-8 col-xl-8'><div class='why-text full-width'><h4>"+value['ProductTitle']+"</h4><h4><del>"+value['StrikePrice']+"</del></h4><h5>"+value['Price']+"</h5><p>"+value['Description']+"</p><a class='btn hvr-hover' href='#'>Add to Cart</a></div></div></div></div>"
                var gridview = "<div class='col-sm-6 col-md-6 col-lg-4 col-xl-4'><div class='products-single fix'><div class='box-img-hover'><div class='type-lb'><p class="+ value['Offer'] +">"+ value['Offer'] +"</p></div><img src="+value['ProductImage']+" class='img-fluid' alt='Image'><div class='mask-icon'><ul><li><a href="""induvialProduct/+value['slug']""" data-toggle='tooltip' data-placement='right' title='View'><i class='fas fa-eye'></i></a></li><li><a href='#' data-toggle='tooltip' data-placement='right' title='Compare'><i class='fas fa-sync-alt'></i></a></li><li><a href='#' data-toggle='tooltip' data-placement='right' title='Add to Wishlist'><i class='far fa-heart'></i></a></li></ul><a class='cart' href='#'>Add to Cart</a></div></div><div class='why-text'><h4>"+value['ProductTitle']+"</h4><h4><del>"+value['StrikePrice']+"</del></h4><h5>"+value['Price']+"</h5></div></div></div>"
                console.log(gridview)
                $('#list-view').append(html);
                $('#inside-grid-view').append(gridview);

                });

                },
            error: function(data){
            }
            });




