import { useState , useEffect} from "react";

const AccountInfo = ({accountId}) =>{
     const [account, setAccount] = useState(null);
   const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  
  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch(`http://127.0.0.1:8000/ecommerce_app/accounts/${accountId}/`);
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        const data = await response.json();
        setAccount(data);
      } catch (error) {
        setError(error.message);
      } finally {
        setLoading(false);
      }

    };
    fetchData();
  }, [accountId]);
    
    
     if (loading) return <div>Loading...</div>;
    if (error) return <div>Error: {error}</div>;

    // Check if account is null before accessing its properties
    if (!account) {
        return <div>No account data available.</div>;
    }
  return (
    <div className="App">
       <div>
            <h2>Account Details</h2>
            <p>ID: {account.userid}</p>
            <p>Username: {account.user_name}</p>
            <p>Email: {account.email}</p>
            {/* Add other fields as necessary */}
        </div>
    </div>
  );
}

export default AccountInfo;