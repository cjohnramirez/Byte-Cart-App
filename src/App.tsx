import { BrowserRouter, Routes, Route } from "react-router-dom";
import NavBar from "./components/NavBar";

function App() {
  const navComponents: { name: string, linkId: string }[] = [
    { name: "Promotions", linkId: "" },
    { name: "Products", linkId: "" },
    { name: "Offers", linkId: "" },
    { name: "About", linkId: "" },
  ];

  return (
    <div>
      <NavBar navComponents={navComponents}/>
    </div>
  )
}

export default App
