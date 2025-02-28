
Step 9.3: Create an API to Fetch Buyers

         Create a new API route: (pages/api/buyers.js)

		import { PrismaClient } from "@prisma/client";

		const prisma = new PrismaClient();

		export default async function handler(req, res) {
 
 	if (req.method === "GET") {
    
		const buyers = await prisma.buyer.findMany({
      
		orderBy: { firstSeen: "desc" },
    	});
    
	res.status(200).json(buyers);
  
     } 

     else {
   
	 res.status(405).json({ message: "Method Not Allowed" });
     }
  }