context 
{
    input phone: string;
    food: {[x:string]:string;}[]?=null;
    destination: {[x:string]:string;}[]?=null;
    date1: string?=null;
    month1: string?=null;
    date2: string?=null;
    month2: string?=null;
    origin: {[x:string]:string;}[]?=null;
    covid_data: string = "";
    covid_query: string="";
    covid: string?=null;
    flight_o: string = "";
    flight_d: string = "";
    flyon: string = "";
    returnon: string = "";
    flight_data: string="";
    activities: string="";
    coffee: string = "";
    coffee_level: string = "";
    message: string = "";
    message_result: string = "";
    hvac: string = "";
    hvac_result: string = "";
}

/**
* External call declarations.
external function send_order(food: {[x:string]:string;}): string;
*/

external function get_covid_data(covid_query: string): string;
external function get_activities(covid_query: string): string;
external function get_cheapest_flight(flight_o: string,flight_d: string,travelon: string,returnon: string): string;
external function make_coffee(coffee_type: string): string;
external function convey_message(message: string): string;
external function control_thermostat(temp: string): string;
external function control_light(light: string): string;
external function update_hvac(hvac: string): string;







/**
* Script.
*/

start node root 
{
    do 
    {
        #connectSafe($phone);
        #waitForSpeech(1000);
        #sayText("Hi, this is Dasha, your AI powered personal assistant, how may I assist you today?"	);
        wait *;
    }    
    transitions 
    {
        travel: goto travel on #messageHasIntent("trip");
        door: goto door on #messageHasIntent("door");
        coffee: goto coffee on #messageHasIntent("cup");
        hvac: goto hvac on #messageHasIntent("cold");
    }
}

digression door
{
    conditions {on #messageHasIntent("door");}
    do 
    {
        #sayText("Sure, I'll convey your message shortly. Is there anything else I can do for you?");
        var text = #getMessageText();
        set $message = text;
        wait *;
    }
    transitions 
    {
       message_door: goto message_door on #messageHasIntent("door");
    }
    

}
node door
{
    do 
    {
        #sayText("Yes, would you like me to convey a message?");
        wait *;
    }
    transitions 
    {
       message_door: goto message_door on #messageHasIntent("yes");
    }
    

}

digression hvac
{
    conditions {on #messageHasIntent("cold");}
    do 
    {
        set $hvac = "It's too cold in here";
        set $hvac_result = external update_hvac($hvac);
        #sayText("Okay, I've increased the temperature from 24.1 degrees to 27 degrees. Is that better?");
        wait *;
    }
    transitions 
    {
       message_door: goto message_door on #messageHasIntent("door");
    }
    

}
node hvac
{
    do 
    {
        set $hvac = "It's too cold in here";
        set $hvac_result = external update_hvac($hvac);
        #sayText("Okay, I've increased the temperature from 24.1 degrees to 27 degrees. Is that better?");
        wait *;
    }
    transitions 
    {
       message_door: goto message_door on #messageHasIntent("door");
    }
    

}

node message_door
{
    do 
    {
        var text = #getMessageText();
        set $message = text;
        #log(text);
        set $message_result = external convey_message($message);
        #sayText("I've conveyed your message! Is there anything else I could do for you?");
        wait *;
    }
    transitions 
    {
       travel: goto travel on #messageHasIntent("trip");
    }
    

}

digression travel
{
    conditions {on #messageHasIntent("trip");}
    do 
    {
        #sayText("Great! Where would you like to go?");
        wait *;
    }
    transitions 
    {
       confirm_destination: goto confirm_destination on #messageHasData("destination");
    }
    onexit
    {
        confirm_destination: do {
        set $destination = #messageGetData("destination");
        set $covid_query = #messageGetData("destination")[0]?.value??"";
        set $flight_d = #messageGetData("destination")[0]?.value??"";
       }
    }

}

node travel
{
    do 
    {
        #sayText("Great! Where would you like to go?");
        wait *;
    }
    transitions 
    {
       confirm_destination: goto confirm_destination on #messageHasData("destination");
    }
    onexit
    {
        confirm_destination: do {
        set $destination = #messageGetData("destination");
        set $covid_query = #messageGetData("destination")[0]?.value??"";
        set $flight_d = #messageGetData("destination")[0]?.value??"";
       }
    }
}


node confirm_destination
{
    do
    {
        #sayText("Perfect. Let me just make sure I got that right. You want to go to ");
        var destination = #messageGetData("destination");
        for (var item in destination)
            {
                #sayText(item.value ?? "and");
            }
        #sayText(" is that right?");
        wait *;
    }
     transitions 
    {
        check_covid: goto check_covid on #messageHasIntent("covid");
        travel_on: goto travel_on on #messageHasIntent("yes");
        travel: goto travel on #messageHasIntent("no");
    }
}


node travel_on
{
    do 
    {
        #sayText("Okay, when would you like to travel?");
        wait *;
    }
    transitions 
    {
       confirm_travel_date: goto confirm_travel_date on #messageHasData("num") and #messageHasData("dates");
    }
    onexit
    {
        confirm_travel_date: do {
        set $date1 = #messageGetData("num")[0]?.value??"";
        set $month1 = #messageGetData("dates")[0]?.value??"";
        set $flyon = (#messageGetData("num")[0]?.value??"")+(#messageGetData("dates")[0]?.value??"");
       }
    }
}

node confirm_travel_date
{
    do
    {
        #sayText("Perfect. Let me just make sure I got that right. You want to travel on ");
        #sayText(#messageGetData("num")[0]?.value??"");
        #sayText(#messageGetData("dates")[0]?.value??"");
        #sayText(" is that right?");
        wait *;
    }
     transitions 
    {
        return_on: goto return_on on #messageHasIntent("yes");
        repeat_order: goto travel_on on #messageHasIntent("no");
    }
}

node return_on
{
    do 
    {
        #sayText("And when would you like to return?");
        wait *;
    }
    transitions 
    {
       confirm_return_date: goto confirm_return_date on #messageHasData("num") and #messageHasData("dates");
    }
    onexit
    {
        confirm_return_date: do {
        set $date2 = #messageGetData("num")[0]?.value??"";
        set $month2 = #messageGetData("dates")[0]?.value??"";
        set $returnon = (#messageGetData("num")[0]?.value??"")+(#messageGetData("dates")[0]?.value??"");
       }
    }
}
node confirm_return_date
{
    do
    {
        #sayText("Perfect. Let me just make sure I got that right. You want to return on ");
        #sayText(#messageGetData("num")[0]?.value??"");
        #sayText(#messageGetData("dates")[0]?.value??"");
        #sayText(" is that right?");
        wait *;
    }
     transitions 
    {
        origin: goto origin on #messageHasIntent("yes");
        return_on: goto return_on on #messageHasIntent("no");
    }
}

node origin
{
    do 
    {
        #sayText("Oh, and where will you be travelling from?");
        wait *;
    }
    transitions 
    {
       confirm_origin: goto confirm_origin on #messageHasData("destination");
    }
    onexit
    {
        confirm_origin: do {
        set $origin = #messageGetData("destination");
        set $flight_o = (#messageGetData("destination")[0]?.value??"");
       }
    }
}

node confirm_origin
{
    do
    {
        #sayText("Perfect. Let me just make sure I got that right. You will be travelling from ");
        var origin = #messageGetData("destination");
        for (var item in origin)
            {
                #sayText(item.value ?? "and");
            }
        #sayText(" is that right?");
        wait *;
    }
     transitions 
    {
        check_covid: goto check_covid on #messageHasIntent("yes");
        confirm_origin: goto confirm_origin on #messageHasIntent("no");
    }
}

digression check_covid {
    conditions {on #messageHasIntent("covid");}
    do {
        var covid_query = $covid_query;
        set $covid_data = external get_covid_data(covid_query);
        #say("covid_report",{covid_data: $covid_data, covid_query: $covid_query});
        wait *;
    }
    transitions {
        
    }
}

node check_covid {
    do {
        var covid_query = $covid_query;
        set $covid_data = external get_covid_data(covid_query);
        #say("covid_report",{covid_data: $covid_data, covid_query: $covid_query});
        #sayText("Are you sure you'd like to travel?");
        wait *;
    }
    transitions {
        check_flights: goto check_flights on #messageHasIntent("yes");
    }
}

node check_flights {
    do {
        set $flight_data = external get_cheapest_flight($flight_o,$flight_d,$flyon,$returnon);
        set $activities = external get_activities($flight_d);
        #say("flight_report",{flight_data: $flight_data});
        #say("activities_report",{flight_data: $activities});
        wait *;
    }
    transitions {
        
    }
}

digression coffee
{
    conditions {on #messageHasIntent("cup");}
    do 
    {
        #sayText("Sure, what kind of coffee would you like?");
        wait *;
    }
    transitions 
    {
       confirm_coffee: goto confirm_coffee on #messageHasData("coffee");
    }
    onexit
    {
        confirm_coffee: do {
        set $coffee = #messageGetData("coffee")[0]?.value??"";
       }
    }

}

node coffee
{
    do 
    {
        #sayText("Sure, what kind of coffee would you like?");
        wait *;
    }
    transitions 
    {
       confirm_coffee: goto confirm_coffee on #messageHasData("coffee");
    }
    onexit
    {
        confirm_coffee: do {
        set $coffee = #messageGetData("coffee")[0]?.value??"";
       }
    }
}

node confirm_coffee
{
    do
    {
        #sayText("Let me just make sure I got that right. You want a ");
        var coffee = #messageGetData("coffee");
        for (var item in coffee)
            {
                #sayText(item.value ?? "and");
            }
        #sayText(" is that right?");
        wait *;
    }
     transitions 
    {
        make_coffee: goto make_coffee on #messageHasIntent("yes");
        coffee: goto coffee on #messageHasIntent("no");
    }
}

node make_coffee
{
    do 
    {
        var coffee = $coffee;
        set $coffee_level = external make_coffee(coffee);
        #sayText("Coming right up!");
        wait *;
    }
    transitions 
    {
       travel: goto travel on #messageHasIntent("trip");
       thermostat: goto confirm_food_order on #messageHasIntent("cold");
       light: goto confirm_food_order on #messageHasIntent("bright");
    }
    onexit
    {
        thermostat: do {
               set $food =  #messageGetData("food", { value: true });
       }
    }

}





digression place_order
{
    conditions {on #messageHasIntent("place_order");}
    do 
    {
        #sayText("Great! What can I get for you today?");
        wait *;
    }
    transitions 
    {
       confirm_food_order: goto confirm_food_order on #messageHasData("food");
    }
    onexit
    {
        confirm_food_order: do {
               set $food =  #messageGetData("food", { value: true });
       }
    }

}

node place_order
{
    do 
    {
        #sayText("Great! What can I get for you today?");
        wait *;
    }
    transitions 
    {
       confirm_food_order: goto confirm_food_order on #messageHasData("food");
    }
    onexit
    {
        confirm_food_order: do {
        set $food = #messageGetData("food");
       }
    }
}


node confirm_food_order
{
    do
    {
        #sayText("Perfect. Let me just make sure I got that right. You want ");
        var food = #messageGetData("food");
        for (var item in food)
            {
                #sayText(item.value ?? "and");
            }
        #sayText(" is that right?");
        wait *;
    }
     transitions 
    {
        order_confirmed: goto payment on #messageHasIntent("yes");
        repeat_order: goto repeat_order on #messageHasIntent("no");
    }
}


node repeat_order
{
    do 
    {
        #sayText("Let's try this again. What can I get for you today?");
        wait *;
    }
    transitions 
    {
       confirm_food_order: goto confirm_food_order on #messageHasData("food");
    }
    onexit
    {
        confirm_food_order: do {
        set $food = #messageGetData("food");
       }
    }
}

node payment
{
    do
    {
        #sayText("Great. Will you be paying at the store?");
        wait *;
    }
     transitions 
    {
        in_store: goto pay_in_store on #messageHasIntent("pay_in_store");
        by_card: goto by_card on #messageHasIntent("pay_by_card");
    }
}

node pay_in_store
{
    do
    {
        #sayText("Your order will be ready in 15 minutes. Once you’re in the store, head to the pickup counter. Anything else I can help you with? ");
        wait *;
    }
     transitions 
    {
        can_help: goto can_help on #messageHasIntent("yes");
        bye: goto success_bye on #messageHasIntent("no");
    }
}

node by_card
{
    do
    {
        #sayText("I'm sorry, I'm just a demo and can't take your credit card number. If okay, would you please pay in store. Your order will be ready in 15 minutes. Anything else I can help you with? ");
        wait *;
    }
     transitions 
    {
        can_help: goto can_help on #messageHasIntent("yes");
        bye: goto success_bye on #messageHasIntent("no");
    }
}

digression soda_on_tap 
{
    conditions {on #messageHasIntent("soda_on_tap");}
    do 
    {
        #sayText("We’ve got Dr. Pepper, Coke Zero, Raspberry Sprite and a mystery flavor. Will you be wanting a soda with your food?");
        wait *;
    }
    transitions 
    {
        place_order: goto place_order on #messageHasIntent("yes");
        can_help_then: goto can_help_then on #messageHasIntent("no");
    }
}

digression food_available 
{
    conditions {on #messageHasIntent("food_available");}
    do 
    {
        #sayText("We’ve got burgers, hot dogs, grilled cheese sandwiches, fries, milkshakes and soda pop. Would you like to order now?");
        wait *;
    }
    transitions 
    {
        place_order: goto place_order on #messageHasIntent("yes");
        can_help_then: goto can_help_then on #messageHasIntent("no");
    }
}

digression delivery 
{
    conditions {on #messageHasIntent("delivery");}
    do 
    {
        #sayText("Unfortunately we only offer pick up service through this channel at the moment. Would you like to place an order for pick up now?");
        wait *;
    }
    transitions 
    {
        place_order: goto place_order on #messageHasIntent("yes");
        can_help_then: goto no_dice_bye  on #messageHasIntent("no");
    }
}

digression connect_me 
{
    conditions {on #messageHasIntent("connect_me");}
    do 
    {
        #sayText("Certainly. Please hold, I will now transfer you. Good bye!");
        #forward("79231017918");
    }
}

node can_help_then 
{
    do
    {
        #sayText("How can I help you then?");
        wait *;
    }
}

node can_help
{
    do
    {
        #sayText("How can I help?");
        wait *;
    }
}

node success_bye 
{
    do 
    {
        #sayText("Thank you so much for your order. Have a great day. Bye!");
        #disconnect();
        exit;
    }
}

digression bye 
{
    conditions { on #messageHasIntent("bye"); }
    do 
    {
        #sayText("Thanks for your time. Have a great day. Bye!");
        #disconnect();
        exit;
    }
}

node no_dice_bye 
{
    do 
    {
        #sayText("Sorry I couldn't help you today. Have a great day. Bye!");
        #disconnect();
        exit;
    }
}