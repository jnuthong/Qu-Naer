__author__ = 'Gong'

from apps.auction.models import Auction

class AuctionLogic(object):
	
	@classmethod
	def create_auction(cls, user_id, place_id, stuff_name, stuff_type,
	 					stuff_describe, start_price):
		return Auction.create_auction(user_id=user_id,
										place_id=place_id,
										stuff_name=stuff_name,
										stuff_type=stuff_type,
										stuff_describe=stuff_describe,
										start_price=start_price,
										)

