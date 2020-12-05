backTest <- function(prices, df, verbose = FALSE){
  if(!all(colnames(df) == c('dates', 'action'))){
    return("Error: Invalid Data Frame Format.")
  }
  
  # Get only rows that we buy or sell from.
  relevant_prices <- prices[df$dates,]
  
  # Initialize starting investment of $1000000.
  investment <- 1000000
  q <- 100
  
  if(verbose){
    print(paste0("Initializing investment at $", investment))
    print("------------------------")
  }
  
  
  # Begin backtesting
  q_total <- 0
  q_cur <- 0
  for (i in seq_along(1:nrow(df))){
    p <- as.numeric(prices[df$dates[i], 6])
    if(length(p) == 0){
      return(NA)
    }
    if(verbose){
      print(paste0("Date: ", df$dates[i]))
    }
    if(df$action[i] == 'buy'){
      q_cur <- floor(investment/p)
      q_total <- q_total + q_cur
      investment <- investment - (p*q_cur)
      if(verbose){
        print(paste0("Bought ", q_cur, " at $", p))
        print(paste0("Investment total: $", round(investment, 2)))
      }
      
    } else {
      investment <- investment + (p*q_total)
      if(verbose){
        print(paste0("Sold ", q_total, " at $", p))
        print(paste0("Investment total: $", round(investment, 2)))
      }
      q_total <- 0
    }
    if(verbose){
      print("------------------------")
    }
  }
  
  # Sell anything leftover
  p <- as.numeric(prices["2020-11-13", 6])
  investment <- investment + p*q_total
  
  if(verbose){
    print(paste0("Final Amount: $", investment))
    print(paste0("Percentage Yield: ", round((investment/1000000), 2) * 100, "%"))
  }
  
  return (100*(investment/1000000))
}