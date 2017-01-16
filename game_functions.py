#!/usr/bin/python
#coding:utf-8

import sys
import pygame
from bullet import Bullet

def check_events(ai_settings,screen,ship,bullets):
	""" 响应鼠标事件 """
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event,ai_settings,screen,ship,bullets)
		elif event.type == pygame.KEYUP:
			chek_keyup_events(event,ai_settings,screen, ship)
# 响应按键按下事件
def check_keydown_events(event,ai_settings,screen,ship,bullets):
	if event.key == pygame.K_RIGHT:
		ship.moving_right =True
	elif event.key == pygame.K_LEFT:
		ship.moving_left = True
	elif event.key == pygame.K_SPACE:
		fire_bullet(ai_settings,screen,ship,bullets)
		
# 响应按键松开事件
def chek_keyup_events(event,ai_settings,screen,ship):
	if event.key == pygame.K_RIGHT:
		ship.moving_right = False
	elif event.key == pygame.K_LEFT:
		ship.moving_left = False

# 绘制屏幕上的内容	
def update_screen(ai_settings,screen,ship,bullets):
	""" 更新屏幕上的图像，并切换到新屏幕"""
	# 每次循环时都会重绘屏幕
	screen.fill(ai_settings.bg_color)
	for bullet in bullets:
		bullet.draw_bullet()
	ship.blitme()
	
	# 让最近绘制的屏幕可见
	pygame.display.flip()
	
# 更新子弹
def update_bullets(bullets):
	bullets.update()
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)
	print(len(bullets))

# 生成子弹
def fire_bullet(ai_settings,screen,ship,bullets):
	if len(bullets) < ai_settings.bullets_allowed:
		new_bullet = Bullet(ai_settings, screen, ship)
		bullets.add(new_bullet)