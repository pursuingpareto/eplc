


import './App.css'
import {Button} from './components/ui/button'
import {
  NavigationMenu,
  NavigationMenuContent,
  NavigationMenuIndicator,
  NavigationMenuItem,
  NavigationMenuLink,
  NavigationMenuList,
  NavigationMenuTrigger,
  NavigationMenuViewport,
} from "./components/ui/navigation-menu"


function App() {


  return (
    <>
       <NavigationMenu>
  <NavigationMenuList>
    <NavigationMenuItem>
        <NavigationMenuLink>Events</NavigationMenuLink>
    </NavigationMenuItem>
    <NavigationMenuLink>About us</NavigationMenuLink>
    <NavigationMenuItem>
    </NavigationMenuItem>
    <NavigationMenuItem>
        <NavigationMenuLink>Contact us</NavigationMenuLink>
    </NavigationMenuItem>
  </NavigationMenuList>
</NavigationMenu>

         <h1 className={"text-3xl font-bold underline"} > Hello </h1>
         <Button> hi</Button>

    </>
  )
}

export default App
