import {
  type RouteConfig,
  route,
} from "@react-router/dev/routes";

export default [
  // * matches all URLs, the ? makes it optional so it will match / as well
  route("*?", "catchall.tsx"),
  route("about", "pages/about.tsx"),
  route("reserve", "pages/reserve.tsx"),
  route("contact", "pages/contact.tsx"),
  route("events", "pages/events.tsx")


] satisfies RouteConfig;
