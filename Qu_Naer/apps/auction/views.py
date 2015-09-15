from django.shortcuts import render
from apps.auction.logic import AuctionLogic

def create_auction(request):
	"""
    Product by G
    REQUIRE_PARAM:
        - user_id
        - place_id
        - stuff_name
        - stuff_type
        - stuff_describe
        - stuff_image
        - start_price
    """
	if request.method == "GET":
        return render(request, "main.html", {})
    else:
    	user_id = None
    	if 'user_id' in request.session:
    		user_id = request.session['user_id']
    		if not user_id:
    			return dict(msg="Please login before create an auction!",
    						warn="OK")
    	else
    		return dict(msg="Please login before create an auction!",
    						warn="OK")
    	place_id = request.POST.get('place_id').encode("utf-8")
    	stuff_name = request.POST.get('stuff_name').encode("utf-8")
    	stuff_type = request.POST.get('stuff_type').encode("utf-8")
    	stuff_describe = request.POST.get('stuff_describe').encode("utf-8")
    	start_price = request.POST.get('start_price').encode("utf-8")

    	rtn = AuctionLogic.create_auction(user_id=user_id,
    										place_id=place_id,
    										stuff_name=stuff_name,
    										stuff_type=stuff_type,
    										stuff_describe=stuff_describe,
    										start_price=start_price,
    										)
    	if rtn['warn'] = 'none':
    		return render()
    	else:
    		return render()







