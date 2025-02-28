This project tracks new buyers on the Solana blockchain and displays them on a Next.js dashboard. It integrates with Solana RPC, PostgreSQL (via Prisma), and TailwindCSS to provide real-time buyer tracking.

-> Project Breakdown
(1) Features & Tech Stack

   -> Features
   (1) Tracks new buyers on Solana
   (2) Filters only first-time buyers
   (3) Stores buyer data in PostgreSQL
   (4) Provides a clean Next.js dashboard

-> Tech Stack
  (1) Solana Web3.js – To interact with the Solana blockchain
  (2) Next.js – For the frontend dashboard and API handling
  (3) Prisma – To manage the PostgreSQL database
  (4) PostgreSQL – To store buyer details
  (5) TailwindCSS – For beautiful UI design

 (2) How It Works
    (a) Fetch buyer transactions from Solana
    (b) Check if they are first-time buyers
    (c) Store buyer details in PostgreSQL
    (d) Create a Next.js API to serve buyer data
    (e) Build a dashboard to display buyers

-> Step-by-Step Implementation
   (a) Step 1: Setup PostgreSQL Database
   (b) We need a PostgreSQL database to store new buyers.

(1) Install PostgreSQL Locally
For Ubuntu/Debian:

sudo apt update
sudo apt install postgresql postgresql-contrib
For macOS (Homebrew):

brew install postgresql
brew services start postgresql
For Windows, download and install PostgreSQL from here.

(2) Create a Database

sudo -u postgres psql
CREATE DATABASE solana_tracker;

 -> Step 2: Set Up Prisma ORM
  Prisma helps us interact with PostgreSQL in Next.js.

(1) Install Prisma
Inside your Next.js project:

npm install @prisma/client @prisma/cli
npx prisma init
This creates a .env file and a prisma/schema.prisma file.

(2) Define Database Schema (prisma/schema.prisma)

generator client {
  provider = "prisma-client-js"
}

datasource db {
  provider = "postgresql"
  url      = env("DATABASE_URL")
}

model Buyer {
  id             Int     @id @default(autoincrement())
  walletAddress  String  @unique
  balance        Float
  firstSeen      DateTime @default(now())
}

(3) Migrate Database

npx prisma migrate dev --name init
This creates the Buyer table in PostgreSQL.

-> Step 3: Track Solana Buyers
We’ll use Solana Web3.js to track new buyers.

(1) Install Solana Web3.js

npm install @solana/web3.js

(2) Create a Script (scripts/trackBuyers.js)

import { Connection, PublicKey } from "@solana/web3.js";
import { PrismaClient } from "@prisma/client";

const connection = new Connection("https://api.mainnet-beta.solana.com");
const prisma = new PrismaClient();

async function fetchBuyers() {
  const programId = new PublicKey("YOUR_SOLANA_PROGRAM_ID"); 

  let transactions = await connection.getConfirmedSignaturesForAddress2(programId, { limit: 10 });

  for (let tx of transactions) {
    let details = await connection.getTransaction(tx.signature);
    
    if (!details || !details.meta) continue;

    let buyer = details.transaction.message.accountKeys[0].toBase58();
    let balance = await connection.getBalance(new PublicKey(buyer)) / 1e9;

    let exists = await prisma.buyer.findUnique({ where: { walletAddress: buyer } });

    if (!exists) {
      await prisma.buyer.create({
        data: { walletAddress: buyer, balance },
      });
      console.log(`New Buyer Added: ${buyer}`);
    }
  }
}

fetchBuyers();

(3) Run the Script

node scripts/trackBuyers.js
This fetches new buyers and stores them in PostgreSQL.

-> Step 4: Create API to Fetch Buyers
We need an API endpoint to fetch buyer data from PostgreSQL.

(1) Create API Route (pages/api/buyers.js)

import { PrismaClient } from "@prisma/client";

const prisma = new PrismaClient();

export default async function handler(req, res) {
  if (req.method === "GET") {
    const buyers = await prisma.buyer.findMany({
      orderBy: { firstSeen: "desc" },
    });
    res.status(200).json(buyers);
  } else {
    res.status(405).json({ message: "Method Not Allowed" });
  }
}
This API returns buyer data as JSON.

-> Step 5: Build Next.js Dashboard
We’ll create a simple UI to display buyers.

(1) Install Tailwind CSS

npm install tailwindcss postcss autoprefixer
npx tailwindcss init -p

(2) Configure Tailwind (tailwind.config.js)

module.exports = {
  content: ["./pages/**/*.{js,ts,jsx,tsx}", "./components/**/*.{js,ts,jsx,tsx}"],
  theme: {
    extend: {},
  },
  plugins: [],
};

(3) Add Tailwind Styles (styles/globals.css)

@tailwind base;
@tailwind components;
@tailwind utilities;

(4) Create Buyer Dashboard (pages/index.js)
 
import { useEffect, useState } from "react";

export default function Home() {
  const [buyers, setBuyers] = useState([]);

  useEffect(() => {
    fetch("/api/buyers")
      .then((res) => res.json())
      .then((data) => setBuyers(data));
  }, []);

  return (
    <div className="min-h-screen bg-gray-100 p-6">
      <h1 className="text-3xl font-bold text-center mb-6">Solana Buyers Tracker</h1>
      <div className="max-w-4xl mx-auto bg-white p-4 rounded-lg shadow">
        <table className="w-full border-collapse">
          <thead>
            <tr className="bg-blue-500 text-white">
              <th className="p-2">Wallet</th>
              <th className="p-2">Balance</th>
              <th className="p-2">First Seen</th>
            </tr>
          </thead>
          <tbody>
            {buyers.map((buyer) => (
              <tr key={buyer.id} className="border-t text-center">
                <td className="p-2">{buyer.walletAddress}</td>
                <td className="p-2">{buyer.balance.toFixed(2)} SOL</td>
                <td className="p-2">{new Date(buyer.firstSeen).toLocaleString()}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}

-> Step 6: Run the Dashboard
       npm run dev
Visit http://localhost:3000 to see tracked buyers!

->  Final Features
  (1)  Real-time Solana Buyer Tracking
  (2)  Database to Avoid Duplicate Alerts
  (3)  Web Dashboard to View Buyers
