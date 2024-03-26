import "./App.css";
import Navbar from "./components/Navbar";
import PostRequestComponent from "./components/PostRequestComponent"; // Import PostRequestComponent
import Button from "./components/ui/button"; // Change this line

function App() {
  return (
    <div className="App">
      <Navbar />
      <PostRequestComponent />
      <Button>Click me</Button>
    </div>
  );
}

export default App;
