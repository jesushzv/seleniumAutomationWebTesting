from booking.book import Booking

with Booking() as bot:
    bot.land_first_page()
    bot.change_currency()
    bot.search_destiny()
    bot.checkin_and_checkout()
    bot.guests()
    bot.search()
    bot.apply_filters()