# -*- coding: utf-8 -*-
import scrapy
import json
from scrapy.exceptions import CloseSpider


class ListingsSpider(scrapy.Spider):
    name = 'listings'
    increment_by = 15
    offset=0
    allowed_domains = ['www.cargurus.com']
    start_urls = ["https://www.cargurus.com/Cars/searchResults.action?zip=44106&inventorySearchWidgetType=BODYSTYLE&searchId=ef514953-df0b-4956-959f-a88c61345e5b&nonShippableBaseline=0&makeIds=42&sortDir=ASC&sourceContext=carGurusHomePageBody&distance=200&minPrice=0&sortType=DEAL_SCORE&endYear=2021&entitySelectingHelper.selectedEntity=bg6&startYear=2005&offset=0&maxResults=15&filtersModified=true"]

    # def start_requests(self):
    #     yield scrapy.Request(url="https://www.cargurus.com/Cars/searchResults.action?zip=44106&inventorySearchWidgetType=BODYSTYLE&searchId=ef514953-df0b-4956-959f-a88c61345e5b&nonShippableBaseline=0&makeIds=1&sortDir=ASC&sourceContext=carGurusHomePageBody&distance=200&minPrice=0&sortType=DEAL_SCORE&endYear=2021&entitySelectingHelper.selectedEntity=bg7&startYear=2005&offset=915&maxResults=15&filtersModified=true", callback=self.parse, headers={
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'
    #     })

    def parse(self, response):
        if self.offset == 1650:
            raise CloseSpider("Last Page reached..")

        resp = json.loads(response.body)

        def check_for_null(key,dictionary):
            if key in dictionary.keys():
                return dictionary[key]
            else:
                return None

        for i in range(len(resp)):
            key = resp[i]

            Accidents = check_for_null('accidentCount',key) 
            Body_type = check_for_null('bodyTypeName',key) 
            Year = check_for_null("carYear",key)
            Fuel_economy_combined = check_for_null("localizedCombinedFuelEconomy",key)
            Days_on_market = check_for_null("daysOnMarket",key)
            Rating = check_for_null("dealRating",key)
            Distance = check_for_null("distance",key)
            Color = check_for_null("normalizedExteriorColor",key)
            Drive_train = check_for_null("DRIVETRAIN",key["filterData"])
            Cylinders = check_for_null("ENGINE_CYLINDERS",key["filterData"])
            Make = check_for_null("makeName",key)
            Mileage = check_for_null("mileage",key) 
            Model = check_for_null("modelName",key) 
            Transmission = check_for_null("localizedTransmission",key)

            if "options" in key.keys():
                Amenities = len(key["options"])
            else:
                Amenities = 0
            
            Owners = check_for_null("ownerCount",key)
            Price_drops = check_for_null("HAS_RECENT_PRICE_DROPS",key["filterData"])
            Photos = check_for_null("HAS_PHOTOS",key["filterData"])
            Seats = check_for_null("SEATING_CAPACITY",key["filterData"])
            Seller = check_for_null("sellerType",key)
            Trim = check_for_null("trimName",key)
            Price = check_for_null("price",key)
            

            
            
            yield {
                "Id": key["id"],
                "Accidents": Accidents,
                "Body_type": Body_type,
                "Year": Year,
                "Fuel_economy_combined": Fuel_economy_combined,
                "Days_on_market": Days_on_market,
                "Rating": Rating,
                "Distance": Distance,
                "Color": Color,
                "Drivetrain": Drive_train,
                "Engine": Cylinders,
                "Make": Make,
                "Mileage": Mileage,
                "Model": Model,
                "Transmission": Transmission,
                "Additional_features": Amenities,
                "Previous_owners": Owners,           
                "Price_drops": Price_drops,
                "Photos": Photos,
                "Seats": Seats,                
                "Seller_type": Seller,
                "Trim": Trim,
                "Price": Price                
            }

        self.offset += self.increment_by
        yield scrapy.Request(
            url = "https://www.cargurus.com/Cars/searchResults.action?zip=44106&inventorySearchWidgetType=BODYSTYLE&searchId=ef514953-df0b-4956-959f-a88c61345e5b&nonShippableBaseline=0&makeIds=42&sortDir=ASC&sourceContext=carGurusHomePageBody&distance=200&minPrice=0&sortType=DEAL_SCORE&endYear=2021&entitySelectingHelper.selectedEntity=bg6&startYear=2005&offset={}&maxResults=15&filtersModified=true".format(self.offset),
            callback=self.parse, headers={
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'
            }
        )



