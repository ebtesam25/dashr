const axios = require("axios");
async function getFlights(flight_o, flight_d, travelon, returnon){
  try {
    var data = JSON.stringify({"origin" : flight_o,
    "destination": flight_d,
    "date" : travelon+"2022",
    "return" : returnon+"2022"
    });
    var config = {
      method: 'post',
      url: 'https://581d-163-118-242-51.ngrok.io/getreturn',
      headers: { 
        'Content-Type': 'application/json'
      },
      data : data
    };
    
  const details = await axios(config);
  console.log(details.data);
  return details.data;
  
  } catch (error) {
      console.error(error);
  }
}

async function getCovidData(covid_query){
    try {
      var state = "";
      var data = JSON.stringify({
        "destination": covid_query
      });
      var config2 = {
        method: 'post',
        url: 'https://581d-163-118-242-51.ngrok.io/getcovidrisk',
        headers: { 
          'Content-Type': 'application/json'
        },
        data : data
      };
      
    const details = await axios(config2);
    console.log(details.data);
     
    var config = {
        method: 'get',
        url: `http://api.positionstack.com/v1/forward?access_key=1119a1059ec9fa013171c331cc661c60&query=${covid_query}`,
        headers: { }
      };
      const response = await axios(config)
      console.log("State:",response.data.data[0].region);
      state=response.data.data[0].region;
      console.log(state);

      const res = await axios.get(`https://disease.sh/v3/covid-19/states/${state}`)
      //console.log("State:",state)
      const report={"res":res.data,"details":details.data}
      return report;
    } catch (error) {
        console.error(error);
    }
}
async function makeBeverage(drink){
  var axios = require('axios');
var data = JSON.stringify({
  "drinktype": drink
});

var config = {
  method: 'post',
  url: 'https://581d-163-118-242-51.ngrok.io/makebeverage',
  headers: { 
    'Content-Type': 'application/json'
  },
  data : data
};

var response = axios(config)
console.log(response.data);

}
async function conveyMessage(message){
  var axios = require('axios');
  var data = JSON.stringify({
  "message": message
});

var config = {
  method: 'post',
  url: 'https://581d-163-118-242-51.ngrok.io/atmydoor',
  headers: { 
    'Content-Type': 'application/json'
  },
  data : data
};

var response = axios(config)
console.log(response.data);

}
async function getActivities(covid_query){
  try {
    
    var data = JSON.stringify({
      "destination": covid_query
    });
    var config = {
      method: 'post',
      url: 'https://581d-163-118-242-51.ngrok.io/gettodos',
      headers: { 
        'Content-Type': 'application/json'
      },
      data : data
    };
    
  const details = await axios(config);
  console.log(details.data.activities);
  activity_str = "";
  var i =0;
  for(i=0;i<5;i++){
    activity_str=activity_str+","+details.data.activities[i];
  }
   return activity_str;
  } catch (error) {
      console.error(error);
  }
}


module.exports = { getCovidData,getFlights,getActivities, makeBeverage, conveyMessage };