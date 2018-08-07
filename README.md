# Ten BackEnd Tech Test

## Shop
There are inital models set up for a Shop application. This repo should be forked with a PR per challenge. Each PR should branch of the previous branch as the rules in earlier challenges carry through.

* Complete as much or as little as you would like of this test, and take as much time as you see fit.
* Please commit as often as possible.
* Feel free to comment on parts of the submitted PR['s] with any assumptions you feel you have made.
* Use any external packages you think may help you complete these challenges.

### Challenge #1
* Allow hat's to have a colour
* Make the brand field on hat's optional 
* Allow for hat's to have an additional style
* Make it so that footwear can have more than one brand 

### Challenge #2
* Make it so that the footwear endpoint does not return style
* On the hat's list endpoint return the brand's name
* On the footwear endpoint return the brand's name and description
* When posting to the hat endpoint require all fields to be entered but when retriving a hat only return the brand and price
* Return both hat's and footwear sorted by cheapest price

### Challenge #3
* Only superusers should be able to write to the hat, footwear and brand endpoints
* All users should be able to read the hat, footwear and brand endpoints

### Challenge #4
* Create a basket book endpoint
    * This endpoint should allow a user to book multiple hats and multiple footwear items in 1 request
    * There should be a total price that sums the price of everything in the basket 
    * There should be a field for total price of hats in the basket
    * There should be a field for total price of footwear in the basket
    * There should be a timestamp to track when the basket book was created and last updated 
* A user should be able to see their own basket books but noone else's
    * The time in which the booking was returned should be displayed
        * The time should be returned in isoformat
* Superusers can see everyones basket books

### Challenge #5
* Create activity tracking
    * An endpoint that displays all user's bookings
        * This endpoint should return all information about the booking including details about each item booked
    * Contains a field to tell the user how long it has been since their last booking
        * The duration should be returned in isoformat
