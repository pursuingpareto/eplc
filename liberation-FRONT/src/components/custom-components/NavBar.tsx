import {
  NavigationMenu,
  NavigationMenuContent,
  NavigationMenuIndicator,
  NavigationMenuItem,
  NavigationMenuLink,
  NavigationMenuList,
  NavigationMenuTrigger,
  NavigationMenuViewport,
} from "../ui/navigation-menu"
import {Link} from 'react-router'

function NavBar() {


  return (
    <>


<NavigationMenu>
<NavigationMenuList>
<Link to={'/about'}><NavigationMenuLink>About us
  </NavigationMenuLink></Link>
  <NavigationMenuItem>
  <Link to={'/reserve'}>
  <NavigationMenuLink>

    Reserve

    </NavigationMenuLink>
    </Link>
  </NavigationMenuItem>
  <NavigationMenuItem>
  <Link to={'/contact'}>
      <NavigationMenuLink>Contact us </NavigationMenuLink> </Link>

  </NavigationMenuItem>
  <NavigationMenuItem>
  <Link to={'events'}>
      <NavigationMenuLink> Events </NavigationMenuLink>
  </Link>
  </NavigationMenuItem>
</NavigationMenuList>
</NavigationMenu>

    </>
  )
}

export default NavBar
