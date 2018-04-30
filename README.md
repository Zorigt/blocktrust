# Insight Data Engineering 18B
**Blocktrust**: In Block-Data We Trust 👁️
## Project Description
Bring transparency to bitcoin transactions and blockchains. Blockchains are immutable public ledger that can be audited, but hardly anyone keeps track of how money is moved  between wallets. Average daily bitcoin transaction volume is roughly **$7,449,010,000** USD as in *BILLIONS* (1). 
## Purpose
Do you want to find out how many bitcoins WikiLeaks received as donation and how they spend it? According to Wikileaks wallet address, they spent it all. As of April 20, 2018 - Wikileaks has mere 0.00001 BTC left in its wallet but they have received about ₿4,042.5 as donations (2). How much is ₿4,042.5 in US Dollars aggregated over time mapped to the exchange rate? How can we trust Wikileaks is ethically spending their funds and for what purposes? Can we track their spending pattern on the blockchain to find out who received all those bitcoins from Wikileaks? 

Wikileaks wallet address 1HB5XMLmzFVj8ALj6mfBsbifRoD4miY36v
- Number of Transactions	26470	
- Total Received	4,042.49832271 BTC	
- Final Balance	0.00001 BTC

So many questions to unearth, but no easy ways to find answers. Bitcoin wallet addresses are public, but it is not human readable or trackable. If average person can't extrabolate information from blockchain, then it servers little purpose on society. 
## Solution
Blockchain an·o·nym·i·ty is a modern problem that requires modern technology to unviel. True democracy requires informed citizens, otherwise they will become a herd of sheep. With my data pipeline using bitcoin blockhain data sets, let's follow the money!
## Data sets
Bitcoin transactions
- File size: 	540 GB
- Rows: 310,686,184

Bitcoin blockchains
- File size: 473 GB
- Rows: 518,934

Combined ~ 1 TB of data to process
## Data Pipeline 
![alt text](/data-pipeline.png)


## What are the primary engineering challenges? -> Why would a Data Engineering Hiring Manager care about this project
- High throughput processing from Kafka broker to Spark stream
- High availabilit database choice and queries for demo
- Overall completeness of the pipeline

## Proposed architecture
S3, Kafka, Spark stream, Cassandra, Flask

## What are the (quantitative) specifications/constraints for this project?
Spec: 
- Query results within 200 millis in Flask

Constraints: 
- Cluster size and count
- Nodes 3-5
- Metrics that can queried from the DB




References <br />
(1) April 20, 2018; https://coinmarketcap.com/currencies/bitcoin/  <br />
(2) April 20, 2018; https://blockchain.info/address/1HB5XMLmzFVj8ALj6mfBsbifRoD4miY36v
