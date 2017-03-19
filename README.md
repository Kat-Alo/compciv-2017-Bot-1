# compciv-2017-first-bot

Given user's birthday, the bot returns the names of California death row inmates 
who were sentenced on the user's birthday and the number of years the inmates
will have been on death row on the user's next birthday.

The bot also returns the temperature high and low in the county where each inmate 
committed their crime, on the date the crime was committed.

The bot only accepts birthdays as 'MM/DD' inputs. Modifications could be added to handle other user date inputs.

An example of how to use this bot:

  import bot
  bot.bot('09/20')
  
output:

  "On your next birthday, VINCENT BROTHERS will have been on California's death row for 10 years, RAYNARD CUMMINGS will have been on California's death row for 32 years, KENNETH GAY will have been on California's death row for 32 years, ERIC HOUSTON will have been on California's death row for 24 years, ALBERT JONES will have been on California's death row for 21 years, BRETT PENSINGER will have been on California's death row for 35 years, BOB WILLIAMS will have been on California's death row for 21 years.There was a high of 99 degrees fahrenheit, and a low of 68 in Kern, where BROTHERS committed their crime on 07/06/2003.There is no weather data for the time and location where JONES committed their crime.There was a high of 75 degrees fahrenheit, and a low of 50 in Kern, where WILLIAMS committed their crime on 10/28/1994.There is no weather data for the time and location where HOUSTON committed their crime.There is no weather data for the time and location where GAY committed their crime.There was a high of 102 degrees fahrenheit, and a low of 57 in San Bernardino, where PENSINGER committed their crime on 08/04/1981.There is no weather data for the time and location where CUMMINGS committed their crime."

The California death row inmate data was parsed separately from the PDF found on the California
state government website: http://www.cdcr.ca.gov/capital_punishment/docs/condemnedinmatelistsecure.pdf.
Because it was not downloaded in the same format that this code handles, the XLSX file is attached.

Additionally, this code assumes that the county where the trial was held is the same county in which
the inmate committed the crime.

The weather data is taken from the Wunderground API. Because Wunderground accepts either zip codes or US state-city combinations
as location inputs, I created a separate XLSX document to map each inmate trial county to a zip code. The zip code was randomly
selected, as there can be many zip codes in any given California county. This, in application, is less problematic because daily
weather conditions likely did not vary greatly within a single county, however the process for creating the spreadsheet
and selecting an arbitrary zip code was not ideal. The spreadsheet is provided in the repository ('zip_codes.xlsl').
