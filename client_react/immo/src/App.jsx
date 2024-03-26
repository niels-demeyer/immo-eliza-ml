import "./App.css";
import PostRequestComponent from "./components/PostRequestComponent"; // Import PostRequestComponent
import Button from "./components/ui/button";
import Choice from "./components/Choice";

function App() {
  return (
    <div className="App">
      <Choice />
      <PostRequestComponent />
      <Button>Click me</Button>
    </div>
  );
}

export default App;
