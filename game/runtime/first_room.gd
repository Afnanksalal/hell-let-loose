extends Node2D

const FLOOR := Rect2(64, 88, 832, 366)
const MARKER_RADIUS := 15.0
const SPEED := 220.0

var marker_position := Vector2(480, 271)
var light_on := true


func _ready() -> void:
	if "--smoke-test" in OS.get_cmdline_user_args():
		for action in [&"move_left", &"move_right", &"move_up", &"move_down", &"interact"]:
			if InputMap.action_get_events(action).is_empty():
				push_error("Missing input binding: %s" % action)
				get_tree().quit(1)
				return
		print("First room ready")
		get_tree().quit()


func _physics_process(delta: float) -> void:
	var direction := Input.get_vector("move_left", "move_right", "move_up", "move_down")
	if direction != Vector2.ZERO:
		var inset := FLOOR.grow(-MARKER_RADIUS)
		marker_position = (marker_position + direction * SPEED * delta).clamp(
			inset.position, inset.end
		)
		queue_redraw()
	if Input.is_action_just_pressed("interact"):
		light_on = not light_on
		queue_redraw()


func _draw() -> void:
	var floor_color := Color("#8f5e59") if light_on else Color("#292c4c")
	var rug_color := Color("#cb8f64") if light_on else Color("#45466e")
	draw_rect(FLOOR, floor_color)
	draw_rect(Rect2(320, 185, 320, 172), rug_color)
	draw_rect(FLOOR, Color("#e6bd91"), false, 2.0)
	draw_circle(marker_position, MARKER_RADIUS + 3.0, Color("#171424"))
	draw_circle(marker_position, MARKER_RADIUS, Color("#ffe1a0"))
