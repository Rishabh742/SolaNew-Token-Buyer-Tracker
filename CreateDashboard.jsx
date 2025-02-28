
Step 9.4: Create the Dashboard Page

      Modify (pages/index.js) to display buyers

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