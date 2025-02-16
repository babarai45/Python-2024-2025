import asyncio
from contextlib import asynccontextmanager
from typing import AsyncGenerator, Dict, List
from dataclasses import dataclass
from datetime import datetime

# --- Data Models ---
@dataclass
class Order:
    id: int
    items: List[str]
    created_at: datetime
    status: str = "created"

# --- Custom Exceptions ---
class KitchenException(Exception):
    pass

# --- Context Managers ---
@asynccontextmanager
async def kitchen_context():
    """Context manager for kitchen resources"""
    print("🏁 Starting kitchen context")
    try:
        # Setup resources asynchronously
        await asyncio.sleep(0.1)  # Simulate resource initialization
        print("✅ Kitchen resources initialized")
        yield "kitchen_resources"
    finally:
        # Cleanup resources asynchronously
        await asyncio.sleep(0.1)  # Simulate cleanup
        print("🧹 Kitchen resources cleaned up")

@asynccontextmanager
async def equipment_monitor():
    """Monitors kitchen equipment status"""
    try:
        print("🔍 Starting equipment monitoring")
        yield
    finally:
        print("⏹️ Stopped equipment monitoring")

# --- Event Loop Management ---
class KitchenEventLoop:
    def __init__(self):
        self.orders: Dict[int, Order] = {}
        self._running = False

    async def start(self):
        """Start the kitchen event loop"""
        self._running = True
        print("🔄 Kitchen event loop started")
        
        async with kitchen_context() as resources:
            async with equipment_monitor():
                while self._running:
                    try:
                        await self.process_orders()
                    except KitchenException as e:
                        await self.handle_error(e)
                    await asyncio.sleep(0.1)  # Prevent CPU overload

    async def process_orders(self):
        """Process pending orders concurrently"""
        async with asyncio.TaskGroup() as tg:
            for order_id, order in self.orders.items():
                if order.status == "created":
                    # Create concurrent tasks for each order
                    tg.create_task(self.process_single_order(order))

    async def process_single_order(self, order: Order):
        """Process a single order with all its components"""
        print(f"🎯 Processing order {order.id}")
        try:
            # Create tasks for different components
            async with asyncio.TaskGroup() as tg:
                # Patty task
                patty_task = tg.create_task(self.cook_patty(order))
                # Fries task
                fries_task = tg.create_task(self.cook_fries(order))
                # Prep task
                prep_task = tg.create_task(self.prep_ingredients(order))

            # Wait for all components to be ready
            await self.assemble_order(order)
            
        except* Exception as exc_group:
            await self.handle_error(exc_group)

    async def cook_patty(self, order: Order) -> None:
        """Coroutine for cooking patty"""
        print(f"🍖 Starting patty for order {order.id}")
        try:
            # Simulate cooking stages
            await asyncio.sleep(0.5)  # Heat up grill
            await asyncio.sleep(1)    # Cook first side
            await asyncio.sleep(1)    # Cook second side
            print(f"✅ Patty done for order {order.id}")
        except Exception as e:
            raise KitchenException(f"Patty cooking failed: {str(e)}")

    async def cook_fries(self, order: Order) -> None:
        """Coroutine for cooking fries"""
        print(f"🍟 Starting fries for order {order.id}")
        try:
            # Simulate cooking stages
            await asyncio.sleep(0.3)  # Heat oil
            await asyncio.sleep(0.8)  # Cook fries
            print(f"✅ Fries done for order {order.id}")
        except Exception as e:
            raise KitchenException(f"Fries cooking failed: {str(e)}")

    async def prep_ingredients(self, order: Order) -> None:
        """Coroutine for preparing ingredients"""
        print(f"🥬 Starting prep for order {order.id}")
        try:
            # Simulate prep stages
            await asyncio.sleep(0.2)  # Get ingredients
            await asyncio.sleep(0.4)  # Cut and prepare
            print(f"✅ Prep done for order {order.id}")
        except Exception as e:
            raise KitchenException(f"Prep failed: {str(e)}")

    async def assemble_order(self, order: Order) -> None:
        """Coroutine for final assembly"""
        print(f"🔄 Assembling order {order.id}")
        try:
            await asyncio.sleep(0.3)  # Assembly time
            order.status = "completed"
            print(f"✅ Order {order.id} assembled and complete")
        except Exception as e:
            raise KitchenException(f"Assembly failed: {str(e)}")

    async def handle_error(self, error) -> None:
        """Error handling coroutine"""
        print(f"❌ Error occurred: {str(error)}")
        # Implement recovery logic here
        await asyncio.sleep(0.1)  # Simulate recovery time

# --- Example Usage ---
async def main():
    """Main entry point"""
    # Create kitchen event loop
    kitchen = KitchenEventLoop()
    
    # Add some test orders
    kitchen.orders[1] = Order(id=1, items=["burger", "fries"], created_at=datetime.now())
    kitchen.orders[2] = Order(id=2, items=["burger"], created_at=datetime.now())
    
    # Start processing
    try:
        await kitchen.start()
    except Exception as e:
        print(f"❌ Main loop error: {str(e)}")

# --- Run the event loop ---
if __name__ == "__main__":
    if not asyncio.get_event_loop().is_running():
        asyncio.run(main())
    else:
        asyncio.run(main())
