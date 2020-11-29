'''A small object oriented Entity-Component-System
'''

from __future__ import annotations
from typing import Dict, List


class EntityFamily:
    """A Filter for a group of components"""

    def __init__(self) -> None:
        self.s_electives = set()
        self.s_included = set()
        self.s_excluded = set()

    def all(self, *components) -> EntityFamily:
        '''Requires an entity to contain all of the components'''
        self.s_included |= set(components)
        return self

    def elective(self, *components) -> EntityFamily:
        '''Requires an entity to contain at least one of the components'''
        self.s_electives |= set(components)
        return self

    def exclude(self, *components) -> EntityFamily:
        '''Requires an entity to contain none of the components'''
        self.s_excluded |= set(components)
        return self

    def matches(self, entity: EntityObject) -> bool:
        '''Checks if an entity matches the family type'''
        keys = set(entity.components.keys())

        if len(self.s_excluded & keys) != 0:
            return False

        if len(self.s_included & keys) == len(self.s_included) and len(self.s_electives) == 0:
            return True

        if len(self.s_electives & keys) > 0:
            return True
        return False

    def create_entity(self, include_electives=False) -> EntityObject:
        '''Creates an entity that satisfies the family'''
        e = EntityObject()
        for c in self.s_included:
            e.attach(c())

        if include_electives:
            for c in self.s_electives:
                e.attach(c())

        return e


class EntityObject:
    '''A holder of components, these can be any type of instantiable class
    '''

    def __init__(self) -> None:
        self.components: Dict[type, object] = {}

    def attach(self, component) -> bool:
        '''Attach or update the component if it doesn't already exist'''
        self.components[type(component)] = component

    def remove(self, component_type: type) -> bool:
        '''Removes the component from the class if it exists'''
        if component_type not in self.components:
            return False
        self.components.pop(component_type)
        return True

    def contains(self, component_type: type) -> bool:
        '''Checks if entity contains component'''
        return component_type in self.components

    def get(self, component_type: type) -> object:
        '''Returns the component'''
        return self.components[component_type]


class EntitySystem:
    '''Bare-bones entity processor class'''

    def __init__(self):
        self.entities: List[EntityObject] = []

    def on_engine_change(self, engine: EntityEngine):
        '''Filters the entities from an engine

        Examples:
            Creates a family type and fetches entities from engine

            family = EntityFamily().all(VelocityComponent, PositionComponent)
            self.entities = engine.fetch(family)
        '''
        pass

    def update(self, engine):
        '''Update loop for fetched entities

        Examples:
            Iter loop over all entities fetched and update their components

            for e in self.entities:
                position_component: PositionComponent = e.get(
                    PositionComponent)
                velocity_component: VelocityComponent = e.get(
                    VelocityComponent)
                position_component.x += velocity_component.dx
                position_component.y += velocity_component.dy

            or

            with multiprocessing.Pool() as pool:
                pool.map(lambda e: self.update_entity(e), self.entities)

        '''
        pass


class EntityEngine:
    '''
    Main class of the framework, manages all entities, systems and listeners.
    '''

    def __init__(self) -> None:
        self.systems: List[EntitySystem] = []
        self.entities: List[EntityObject] = []

    def fetch(self, family: EntityFamily):
        '''Returns a list of entities that match the family filter'''
        return filter(lambda e: family.matches(e), self.entities)

    def notify_entity_change(self):
        '''Updates the entities of all systems'''
        for s in self.systems:
            s.on_engine_change(self)

    def add_entity(self, entity: EntityObject, notify_change=True):
        '''Adds an an entity and updates all systems'''
        self.entities.append(entity)
        if notify_change:
            self.notify_entity_change()

    def remove_entity(self, entity: EntityObject, notify_change=True):
        '''Removes an an entity and updates all systems'''
        self.entities.remove(entity)
        if notify_change:
            self.notify_entity_change()

    def update(self) -> None:
        '''Updates all systems'''
        for s in self.systems:
            s.update(self)
