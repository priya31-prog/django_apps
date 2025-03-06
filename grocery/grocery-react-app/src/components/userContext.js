import React ,{ useState, createContext, useContext } from 'react';


 const userContext = createContext();

function Context1() {
    const [user, setUser] = useState('John')
    // setUser('John')
   
    
    return (
        <userContext.Provider value={user}>
            <h1>HEllo user name..{user}</h1>
            <Context2 user={user} />
        </userContext.Provider>
    );
    
}

function Context2() {
    const user = useContext(userContext);
    return (
        <h3>Hello {user}</h3>
    );
}

export default Context1;