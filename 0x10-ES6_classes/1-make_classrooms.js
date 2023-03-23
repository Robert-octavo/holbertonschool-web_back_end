/*
Import the ClassRoom class from 0-classroom.js.

Implement a function named initializeRooms. It should return an array
of 3 ClassRoom objects with the sizes 19, 20, and 34 (in this order).
*/

import ClassRoom from './0-classroom';

export default function initializeRooms() {
  const rooms = [];
  rooms.push(new ClassRoom(19));
  rooms.push(new ClassRoom(20));
  rooms.push(new ClassRoom(34));
  return rooms;
}
