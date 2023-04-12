import { Route, Switch } from "react-router";
import Home from "./Home";
import Navbar from "./Navbar";
import Episode from "./Episode";

function App() {
  return (
    <>
      <Navbar />
      <Switch>
        <Route exact path="/episodes/:id">
          <Episode />
        </Route>
        <Route exact path="/">
          <Home />
        </Route>
      </Switch>
    </>
  );
}

export default App;
