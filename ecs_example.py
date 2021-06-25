from sutil.utils.ecs import *


class IdentifierComponent():
    _instance_index = 0

    def __init__(self) -> None:
        self.id = IdentifierComponent._instance_index
        IdentifierComponent._instance_index += 1


class PositionComponent():
    def __init__(self, x=0, y=0) -> None:
        self.x = x
        self.y = y


class VelocityComponent():
    def __init__(self, dx, dy) -> None:
        self.dx = dx
        self.dy = dy


class MapTileComponent():
    def __init__(self) -> None:
        self.px = 0
        self.py = 0
        self.time = 0


class MoveSystem(EntitySystem):
    def on_engine_change(self, engine: EntityEngine):
        family = EntityFamily().all(VelocityComponent, PositionComponent)
        self.entities = engine.fetch(family)
        pass

    def update(self, engine: EntityEngine):
        for entity in self.entities:
            position_component: PositionComponent = entity.get(
                PositionComponent)
            velocity_component: VelocityComponent = entity.get(
                VelocityComponent)
            position_component.x += velocity_component.dx
            position_component.y += velocity_component.dy
            # print(f"Moved from ({position_component.x -velocity_component.dx}, {position_component.y - velocity_component.dy}) to ({position_component.x}, {position_component.y})")


class PrintNameSystem(EntitySystem):
    def on_engine_change(self, engine: EntityEngine):
        family = EntityFamily().all(IdentifierComponent)
        self.entities = engine.fetch(family)

    def update(self, engine: EntityEngine):
        for entity in self.entities:
            identifier_component: IdentifierComponent = entity.get(
                IdentifierComponent)
            identifier_component.id = 999


class PositionRounderSystem(EntitySystem):
    def on_engine_change(self, engine: EntityEngine):
        family = EntityFamily().all(PositionComponent)
        self.entities = engine.fetch(family)

    def update(self, engine: EntityEngine):
        for entity in self.entities:
            p_component: PositionComponent = entity.get(
                PositionComponent)
            p_component.x = round(p_component.x)
            p_component.y = round(p_component.x)


class FrictionSystem(EntitySystem):
    def on_engine_change(self, engine: EntityEngine):
        family = EntityFamily().all(VelocityComponent)
        self.entities = engine.fetch(family)

    def update(self, engine: EntityEngine):
        for entity in self.entities:
            p_component: VelocityComponent = entity.get(
                VelocityComponent)
            p_component.dx *= 0.998
            p_component.dy *= 0.998


class TileUpdateSystem(EntitySystem):
    def on_engine_change(self, engine: EntityEngine):
        family = EntityFamily().all(MapTileComponent)
        self.entities = engine.fetch(family)

    def update(self, engine: EntityEngine):
        for entity in self.entities:
            tile_component: MapTileComponent = entity.get(
                MapTileComponent)
            tile_component.time += 1


if __name__ == "__main__":
    from random import randint, getrandbits
    import time
    ecs_engine = EntityEngine()
    ecs_engine.systems = [MoveSystem(), PrintNameSystem(),
                          PositionRounderSystem(), FrictionSystem(), TileUpdateSystem()]

    for x in range(100):
        e = EntityObject()
        e.attach(PositionComponent(randint(-100, 100), randint(-100, 100)))
        e.attach(VelocityComponent(getrandbits(8), getrandbits(8)))
        ecs_engine.add_entity(e, False)

    for x in range(10000):
        e = EntityObject()
        e.attach(MapTileComponent())
        e.attach(VelocityComponent(getrandbits(8), getrandbits(8)))
        ecs_engine.add_entity(e, False)

    ecs_engine.notify_entity_change()

    start = time.time()
    n = 0
    while time.time() - start < 1:
        ecs_engine.update()
        n += 1

    print(n/60)

    for e in ecs_engine.entities:
        print("Entity:")
        print([v.__dict__ for v in e.components.values()])
        print()
        time.sleep(0.5)
