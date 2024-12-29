import anvil.server
@anvil.server.callable


def calculate_gravitational_force(m1, m2, r):
  G = 6.61 * pow(10, -11)
  gravity = (G *m1 *m2) / (r*r)
  gravity = round(gravity, 3)
  return gravity

@anvil.server.callable
def calculate_orbit_escape_velocity(m1, r, velocity_number):
  G = 6.61 * pow(10, -11)
  velocity = (velocity_number * G *m1) / r
  velocity = pow(velocity, 0.5)
  velocity = round(velocity, 3)
  return velocity