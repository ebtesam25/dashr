const dasha = require("@dasha.ai/sdk");
const fs = require("fs");
const { getCovidData, getFlights, getActivities, makeBeverage, conveyMessage } = require("./app/api");

async function main() {
  const app = await dasha.deploy("./app");

  app.connectionProvider = async (conv) =>
    conv.input.phone === "chat"
      ? dasha.chat.connect(await dasha.chat.createConsoleChat())
      : dasha.sip.connect(new dasha.sip.Endpoint("default"));

  app.ttsDispatcher = () => "dasha";

  app.setExternal("get_covid_data", async (args)=> {
    let data = await getCovidData(args.covid_query);
    console.log(data);
    let risk = data.details.risk;
    let summary = data.details.summary;
    return "\n There is "+risk+" risk."+summary;
    
    
  });

  app.setExternal("get_cheapest_flight", async (args)=> {
    let data = await getFlights(args.flight_o,args.flight_d,args.travelon,args.returnon);
    console.log(data);
    let flight = data.flight;
    console.log("Flight",flight.type);
    
    return "\n The cheapest flight costs"+data.cheapest+"dollars."
    //"at"+data.JSON.parse(flight).segments[0].departure.iataCode+"and arrives at"+data.JSON.parse(flight).segments[0].arrival.iataCode+"at"+data.JSON.parse(flight).segments[0].arrival.at;
    
    
  });

  app.setExternal("get_activities", async (args)=> {
    let data = await getActivities(args.covid_query);
    console.log(data);
    
    
    return "\n Here's a list of places you should check out on your trip. "+data
    
    
  });

  app.setExternal("make_coffee", async (args)=> {
    let data = await makeBeverage(args.coffee_type);
    console.log(data);
    
    
    return "\n Your coffee is ready!"
    
    
  });

  app.setExternal("convey_message", async (args)=> {
    let data = await conveyMessage(args.message);
    console.log(data);
    
    
    return "\n Your message has been conveyed!"
    
    
  });


  await app.start();

  const conv = app.createConversation({ phone: process.argv[2] ?? "" });

  if (conv.input.phone !== "chat") conv.on("transcription", console.log);

  const logFile = await fs.promises.open("./log.txt", "w");
  await logFile.appendFile("#".repeat(100) + "\n");

  conv.on("transcription", async (entry) => {
    await logFile.appendFile(`${entry.speaker}: ${entry.text}\n`);
  });

  conv.on("debugLog", async (event) => {
    if (event?.msg?.msgId === "RecognizedSpeechMessage") {
      const logEntry = event?.msg?.results[0]?.facts;
      await logFile.appendFile(JSON.stringify(logEntry, undefined, 2) + "\n");
    }
  });

  const result = await conv.execute();

  console.log(result.output);

  await app.stop();
  app.dispose();

  await logFile.close();
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
